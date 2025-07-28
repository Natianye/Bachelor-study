import os
import pandas as pd
import numpy as np
from openai import AzureOpenAI
import time

print("Script started")

# --- Configuration ---
CSV_PATH = os.path.abspath('./data/chunks_for_embedding.csv')
CHUNK_COLUMN = "content"
EMBEDDING_DEPLOYMENT = "text-embedding-3-small"

# --- Initialize Azure OpenAI client ---
client = AzureOpenAI(
    api_key="",  # Replace with your key
    azure_endpoint="",  # Replace with your endpoint
    api_version="2024-10-21"
)

# --- Load Chunks ---
df = pd.read_csv(CSV_PATH)
chunks = df[CHUNK_COLUMN].tolist()

# --- Generate Embeddings ---
def get_embedding(text, deployment_name=EMBEDDING_DEPLOYMENT):
    while True:
        try:
            response = client.embeddings.create(
            input=text,
            model=deployment_name  
            )

            return response.data[0].embedding
        except Exception as e:
            print(f"Error: {e}. Retrying in 2 seconds...")
            time.sleep(2)

embeddings = []
for i, chunk in enumerate(chunks):
    embedding = get_embedding(chunk)
    embeddings.append(embedding)
    if (i + 1) % 10 == 0 or (i + 1) == len(chunks):
        print(f"Embedded {i + 1} / {len(chunks)} chunks")

# --- Convert to numpy array and save ---
embedding_array = np.array(embeddings, dtype=np.float32)
np.save(os.path.abspath('./data/chunk_embeddings.npy'), embedding_array)
print("Embeddings saved to data/chunk_embeddings.npy")
