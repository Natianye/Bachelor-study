import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 12})

# Load your CSV
df = pd.read_csv("./data/results/retrieval_ranks_results.csv")
df["human_original_rank"] = pd.to_numeric(df["human_original_rank"], errors="coerce")
ranks = df["human_original_rank"].dropna()

# Force x-axis and bins to go up to 95
max_rank = 95
bins = np.arange(0, max_rank + 5, 5)

# Plot histogram
plt.figure(figsize=(10, 6))
counts, bins, patches = plt.hist(ranks, bins=bins, edgecolor='black', color='steelblue')

# Title and labels
plt.title("Histogram of Ranks Retrieved by Human-Written Questions")
plt.xlabel("Rank of Original Context Trunk")
plt.ylabel("Frequency")

# Set x-axis ticks every 5 units up to 95
plt.xticks(np.arange(0, max_rank + 5, 5))

# Add counts on top of bars
for count, patch in zip(counts, patches):
    if count > 0:
        plt.text(patch.get_x() + patch.get_width() / 2, count + 1, int(count),
                 ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()
