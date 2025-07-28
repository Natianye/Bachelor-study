import os
import pandas as pd
import numpy as np
from openai import AzureOpenAI
from numpy.linalg import norm

# --- Configuration ---
CSV_PATH = os.path.abspath('./data/chunks_for_embedding.csv')
EMBEDDINGS_PATH = os.path.abspath('./data/chunk_embeddings.npy')
CHUNK_COLUMN = "content"
EMBEDDING_DEPLOYMENT = "text-embedding-3-small"
TOP_K = 10

# --- Initialize Azure OpenAI client ---
client = AzureOpenAI(
    api_key=" ",  # Replace with your key
    azure_endpoint=" ",  # Replace with your endpoint
    api_version="2024-10-21"
)

# --- Load Data ---
df = pd.read_csv(CSV_PATH)
chunks = df[CHUNK_COLUMN].tolist()
embeddings = np.load(EMBEDDINGS_PATH)

# --- Retrieval Function ---
def get_query_embedding(query):
    response = client.embeddings.create(
        input=query,
        model=EMBEDDING_DEPLOYMENT
    )
    return np.array(response.data[0].embedding, dtype=np.float32)

def retrieve_top_k(query, k=TOP_K):
    query_emb = get_query_embedding(query)
    similarities = embeddings @ query_emb / (norm(embeddings, axis=1) * norm(query_emb) + 1e-8)
    top_k_idx = np.argsort(similarities)[-k:][::-1]
    top_chunks = [chunks[i] for i in top_k_idx]
    return top_k_idx, top_chunks

def retrieve_all_ordered_indices(query):
    query_emb = get_query_embedding(query)
    similarities = embeddings @ query_emb / (np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_emb) + 1e-8)
    ordered_idx = np.argsort(similarities)[::-1]
    return ordered_idx

# --- Generation Function ---
def generate_answer(query, retrieved_chunks):
    context = "\n\n".join(retrieved_chunks)
    prompt = f"""You are an expert assistant to answer quation about BayBE. Use the following context to answer the question. All the contexts are from BayBE documentation.
Context:
{context}

Question: {query}

Answer:"""
    response = client.chat.completions.create(
        model="gpt-41-gs",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=512,
        temperature=0.2
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    query = input("Please enter your question: ")
    chunk_indices, top_chunks = retrieve_top_k(query)
    
    print("\nRetrieved chunk indices and their content:")
    for idx, chunk in zip(chunk_indices, top_chunks):
        print(f"Index: {idx}\nChunk: {chunk}\n{'-'*40}")
        
    answer = generate_answer(query, top_chunks)
    print("Generated Answer:\n", answer)
