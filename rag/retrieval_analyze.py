import pandas as pd
import ast

# --- Load Data ---
df = pd.read_csv('retrieval_ranks_results.csv')

# --- Parse Indices Columns ---
def parse_indices(cell):
    py_list = ast.literal_eval(cell)
    return [int(x) for x in py_list]

df['human_indices'] = df['human_indices'].apply(parse_indices)
df['synthetic_indices'] = df['synthetic_indices'].apply(parse_indices)

# --- Compute Overlap Counts ---
def top_k_overlap(row, k):
    topk_human = set(row['human_indices'][:k])
    topk_synth = set(row['synthetic_indices'][:k])
    return len(topk_human & topk_synth)

df['top5_overlap_count'] = df.apply(lambda row: top_k_overlap(row, 5), axis=1)
df['top10_overlap_count'] = df.apply(lambda row: top_k_overlap(row, 10), axis=1)

# --- Compute Recall@K ---
def recall_at_k(rank, k):
    return int(rank is not None and rank <= k)

for k in [1, 3, 5, 10]:
    df[f'human_recall@{k}'] = df['human_original_rank'].apply(lambda r: recall_at_k(r, k))
    df[f'synthetic_recall@{k}'] = df['synthetic_original_rank'].apply(lambda r: recall_at_k(r, k))

# --- Compute MAP ---
def average_precision(rank):
    return 1.0 / rank if rank is not None else 0.0

df['human_ap'] = df['human_original_rank'].apply(average_precision)
df['synthetic_ap'] = df['synthetic_original_rank'].apply(average_precision)

# --- Summary Statistics ---
avg_top5_overlap = df['top5_overlap_count'].mean()
avg_top10_overlap = df['top10_overlap_count'].mean()
human_map = df['human_ap'].mean()
synthetic_map = df['synthetic_ap'].mean()

print(f'Average Top-5 Overlap: {avg_top5_overlap:.3f}')
print(f'Average Top-10 Overlap: {avg_top10_overlap:.3f}')
print(f'Human MAP: {human_map:.3f}')
print(f'Synthetic MAP: {synthetic_map:.3f}')

for k in [1, 3, 5, 10]:
    human_recall = df[f'human_recall@{k}'].mean()
    synth_recall = df[f'synthetic_recall@{k}'].mean()
    print(f'Human Recall@{k}: {human_recall:.3f}')
    print(f'Synthetic Recall@{k}: {synth_recall:.3f}')

# --- (Optional) Save the augmented DataFrame ---
df.to_csv('retrieval_ranks_results_with_overlap_and_metrics.csv', index=False)
