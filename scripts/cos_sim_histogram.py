import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 12})
# Load your CSV
df = pd.read_csv("./data/results/cosine_sim_results_top5_excel.csv")
df["Human_Cosine_Similarity"] = pd.to_numeric(df["Human_Cosine_Similarity"], errors="coerce")
ranks = df["Human_Cosine_Similarity"].dropna()

if ranks.empty:
    print("No valid data to plot.")
else:
    # Define bins from 0.0 to 1.0 with step 0.1
    bins = np.arange(0.0, 1.1, 0.1)

    plt.figure(figsize=(6, 10))
    counts, bins, patches = plt.hist(
        ranks, 
        bins=bins, 
        edgecolor='black', 
        color='steelblue', 
        orientation='horizontal', 
        alpha=1
    )

    plt.title("Cosine Similarity (Top 5 Retrieval, Human-Written Data)")
    plt.xlabel("Frequency")
    plt.ylabel("Cosine Similarity Score")
    plt.yticks(bins)

    # Set x-axis ticks at 0, 5, 10, 15, 20
    plt.xticks([0, 5, 10, 15, 20])

    # Add vertical grid lines at these ticks
    plt.grid(axis='x', which='major', linestyle='--', alpha=0.7)

    # Annotate bars
    for count, patch in zip(counts, patches):
        if count > 0:
            plt.text(count + 0.2, patch.get_y() + patch.get_height()/2, int(count),
                     va='center', fontsize=10)

    plt.tight_layout()
    plt.show()
