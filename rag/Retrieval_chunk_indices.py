import os
import pandas as pd
from retrieval_generation import retrieve_all_ordered_indices

QUESTIONS_PATH = os.path.abspath('./data/both_qa_for_power_point.csv')
qa_df = pd.read_csv(QUESTIONS_PATH, encoding='latin1')

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

results = []

for idx, row in qa_df.iterrows():
    chunk_id_1based = row['chunk_id']
    human_q = row['Human_Questions']
    synthetic_q = row['gpt_41_gs_question']
    
    if str(human_q).strip().lower() == "no":
        continue

    # Convert chunk_id to 0-based for comparison
    chunk_id = chunk_id_1based - 1

    human_indices = retrieve_all_ordered_indices(fix_mojibake(human_q))
    synthetic_indices = retrieve_all_ordered_indices(fix_mojibake(synthetic_q))

    try:
        human_rank = list(human_indices).index(chunk_id) + 1
    except ValueError:
        human_rank = None
    try:
        synthetic_rank = list(synthetic_indices).index(chunk_id) + 1
    except ValueError:
        synthetic_rank = None

    results.append({
        'chunk_id': int(chunk_id),
        'human_question': human_q,
        'synthetic_question': synthetic_q,
        'human_indices': [int(i) for i in human_indices],
        'synthetic_indices': [int(i) for i in synthetic_indices],
        'human_original_rank': human_rank,
        'synthetic_original_rank': synthetic_rank
    })


# Save to DataFrame and CSV
results_df = pd.DataFrame(results)
results_df.to_csv('./retrieval_ranks_results.csv', index=False)