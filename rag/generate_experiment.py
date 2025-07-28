import numpy as np
import pandas as pd
from retrieval_generation import get_query_embedding, retrieve_top_k, generate_answer


QA_CSV_PATH = './data/both_qa_for_power_point.csv' 
# Change column names if needed
QA_ID_COL = 'QA_id'  
HUMAN_Q_COL = 'Human_Questions'
HUMAN_REF_COL = 'Human_Answers'
SYNTH_Q_COL = 'gpt_41_gs_question'
SYNTH_REF_COL = 'gpt_41_gs_answer'

qa_df = pd.read_csv(QA_CSV_PATH, encoding='latin1')

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

filtered_qa_df = qa_df[
    qa_df[HUMAN_REF_COL].notnull() &                                
    (qa_df[HUMAN_REF_COL].str.strip() != "") &                   
    (qa_df[HUMAN_REF_COL].str.lower().str.strip() != "no")         
]

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-8)

results = []

for idx, row in filtered_qa_df.iterrows():
    qa_id = row[QA_ID_COL]  # Get the QA ID
    human_q = row[HUMAN_Q_COL]
    synthetic_q = row[SYNTH_Q_COL]
    human_ref = str(row[HUMAN_REF_COL])
    synthetic_ref = str(row[SYNTH_REF_COL])

    # Human question/answer
    _, human_chunks = retrieve_top_k(fix_mojibake(human_q))
    human_pred = generate_answer(human_q, human_chunks)
    human_pred_emb = get_query_embedding(human_pred)
    human_ref_emb = get_query_embedding(fix_mojibake(human_ref))
    human_sim = cosine_similarity(human_pred_emb, human_ref_emb)

    # Synthetic question/answer
    _, synth_chunks = retrieve_top_k(synthetic_q)
    synth_pred = generate_answer(synthetic_q, synth_chunks)
    synth_pred_emb = get_query_embedding(synth_pred)
    synth_ref_emb = get_query_embedding(synthetic_ref)
    synth_sim = cosine_similarity(synth_pred_emb, synth_ref_emb)

    # Store results for CSV
    results.append({
        QA_ID_COL: qa_id,
        'Human_Cosine_Similarity': human_sim,
        'Synthetic_Cosine_Similarity': synth_sim,
        HUMAN_Q_COL: human_q,
        HUMAN_REF_COL: human_ref,
        'Human_Prediction': human_pred,
        SYNTH_Q_COL: synthetic_q,
        SYNTH_REF_COL: synthetic_ref,
        'Synthetic_Prediction': synth_pred
    })

    print(f"\nRow {idx}:")
    print(f"  QA ID: {qa_id}")
    print(f"  Human Q: {human_q}")
    print(f"  Human Pred: {human_pred}")
    print(f"  Human Ref: {human_ref}")
    print(f"  Human Cosine Similarity: {human_sim:.4f}")
    print(f"  Synthetic Q: {synthetic_q}")
    print(f"  Synthetic Pred: {synth_pred}")
    print(f"  Synthetic Ref: {synthetic_ref}")
    print(f"  Synthetic Cosine Similarity: {synth_sim:.4f}")
    print("-" * 60)

# Save results to CSV
results_df = pd.DataFrame(results)
results_df.to_csv('./qa_cosine_sim_results.csv', index=False)
print("Results saved to ./qa_cosine_sim_results.csv")

# Optionally, print summary statistics
human_similarities = results_df['Human_Cosine_Similarity']
synthetic_similarities = results_df['Synthetic_Cosine_Similarity']

print(f"\nAverage Human Cosine Similarity: {np.mean(human_similarities):.4f}")
print(f"Average Synthetic Cosine Similarity: {np.mean(synthetic_similarities):.4f}")
