import pandas as pd
import os

# Load your CSV file
df = pd.read_csv(os.path.abspath('./data/All_questions_for_count.csv'))

def count_tokens(text):
    if pd.isnull(text):
        return 0
    return len(str(text).split())

results = []

# Human questions: skip "No"
human_filtered = df[df['Human_Questions'] != "No"]
columns = ['Human_Questions']

# 4o and 41: use all rows, just dropna
columns += ['gpt_4o_mini_question', 'gpt_41_gs_question']

for col in columns:
    if col == 'Human_Questions':
        lengths = human_filtered[col].dropna().apply(count_tokens)
    else:
        lengths = df[col].dropna().apply(count_tokens)
    filtered_lengths = lengths[lengths > 1]
    total = filtered_lengths.count()
    avg = filtered_lengths.mean()
    min_len = filtered_lengths.min()
    max_len = filtered_lengths.max()
    results.append({
        'Query Type': col,
        'Total Queries (>1)': total,
        'Average Length': avg,
        'Minimum Length (>1)': min_len,
        'Maximum Length': max_len
    })

pd.set_option('display.max_columns', None)
results_df = pd.DataFrame(results)
print(results_df)
