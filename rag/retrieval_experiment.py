import pandas as pd
from retrieval_generation import retrieve_all_ordered_indices
import os

# --- Experiment Parameters ---
QUESTIONS_PATH = os.path.abspath('./data/both_qa_for_power_point.csv')

def fix_mojibake(text):
    if isinstance(text, str):
        try:
            return text.encode('latin-1').decode('utf-8')
        except Exception:
            try: 
                return text.encode('windows-1252').decode('utf-8')
            except Exception:
                return text
    return text


TOP_X = 10  # Set this to your desired value

# --- Load Questions ---
qa_df = pd.read_csv(QUESTIONS_PATH, encoding='latin1')



# --- Results Storage ---
overlap_counts = []
human_top_1_count = 0
synthetic_top_1_count = 0
human_original_ranks = []
synthetic_original_ranks = []
human_recalls = []
synthetic_recalls = []
processed_chunk_ids = []

for idx, row in qa_df.iterrows():
    chunk_id = row['chunk_id']
    human_q = row['Human_Questions']
    synthetic_q = row['gpt_41_gs_question']
    
    if str(human_q).strip().lower() == "no":
        continue
    
    processed_chunk_ids.append(chunk_id)

    # Retrieve top X for both questions
    human_indices = retrieve_all_ordered_indices(human_q)
    synthetic_indices = retrieve_all_ordered_indices(synthetic_q)

    #Overlap in top X
    overlap = len(set(human_indices) & set(synthetic_indices))
    overlap_counts.append(overlap)

    # Check if original chunk is top-1 for each question
    if human_indices[0] == chunk_id:
        human_top_1_count += 1
    if synthetic_indices[0] == chunk_id:
        synthetic_top_1_count += 1

    # Calculate rank of original chunk in each retrieval
    try:
        human_rank = list(human_indices).index(chunk_id) + 1  # +1 for 1-based rank
    except ValueError:
        human_rank = None
    try:
        synthetic_rank = list(synthetic_indices).index(chunk_id) + 1
    except ValueError:
        synthetic_rank = None

    human_original_ranks.append(human_rank)
    synthetic_original_ranks.append(synthetic_rank)
    
    # Recall@k for each
    human_recalls.append(int(chunk_id in human_indices))
    synthetic_recalls.append(int(chunk_id in synthetic_indices))

# --- Calculate Averages ---
def average_rank(ranks):
    valid_ranks = [r for r in ranks if r is not None]
    return sum(valid_ranks) / len(valid_ranks) if valid_ranks else None

avg_human_rank = average_rank(human_original_ranks)
avg_synth_rank = average_rank(synthetic_original_ranks)
average_recall_at_k_human = sum(human_recalls) / len(human_recalls)
average_recall_at_k_synth = sum(synthetic_recalls) / len(synthetic_recalls)

# --- Save Results ---
results_df = pd.DataFrame({
    'chunk_id': processed_chunk_ids,
    'overlap_in_top_X': overlap_counts,
    'human_top1': [int(r == 1) if r is not None else 0 for r in human_original_ranks],
    'synthetic_top1': [int(r == 1) if r is not None else 0 for r in synthetic_original_ranks],
    'human_rank': human_original_ranks,
    'synthetic_rank': synthetic_original_ranks,
})

results_df.to_csv('./data/retrieval_experiment_results_top10.csv', index=False)

# --- Print Summary ---
print(f"Human questions: original chunk retrieved as top-1 in {human_top_1_count} cases.")
print(f"Synthetic questions: original chunk retrieved as top-1 in {synthetic_top_1_count} cases.")
print(f"Average rank of original chunk (human): {avg_human_rank:.2f}")
print(f"Average rank of original chunk (synthetic): {avg_synth_rank:.2f}")
print(f"\nAverage Human Recall@{TOP_X}: {average_recall_at_k_human:.3f}")
print(f"Average Synthetic Recall@{TOP_X}: {average_recall_at_k_synth:.3f}")