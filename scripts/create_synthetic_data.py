import os
from openai import AzureOpenAI
import pandas as pd
from time import sleep

# Initialize OpenAI client
client = AzureOpenAI(
    api_key= "55a6f00f-0e01-4a39-85de-3bb90460d96f",
    azure_endpoint = "https://api.nlp.p.uptimize.merckgroup.com",
    api_version="2024-10-21" # Pass Based on Model Version
)

# File paths
input_csv = os.path.abspath('./data/human_qa_for_synthetic_qa.csv')
output_csv = os.path.abspath('./data/synthetic_qa_version3.csv')

# Load the input CSV
df = pd.read_csv(input_csv, encoding='latin1')

# Function to generate Q&A for a single context
def generate_qa(context):
    prompt = f"""Your task is to write a factoid question and an answer given a context. All the contexts are from BayBE documentation.
Your factoid question should be answerable with a specific, concise piece of factual information from the context.
Your factoid question should be formulated in the same style as questions BayBE users could ask in a search engine.
Your factoid question must be reasonable and must be understood and responded to by humans.
This means that your factoid question MUST NOT mention something like "according to the passage" or "context".

Context:
\"\"\"{context}\"\"\"

Return:
Q: <question>
A: <answer>
"""
    try:
        response = client.chat.completions.create(
            model="gpt-41-gs",  
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=300
        )
        
        # print (response)
        
        content = response.choices[0].message.content.strip()

        # Split into Q and A
        lines = content.split("\n")
        q = next((line[3:].strip() for line in lines if line.strip().lower().startswith("q:")), "N/A")
        a = next((line[3:].strip() for line in lines if line.strip().lower().startswith("a:")), "N/A")
        return q, a
    except Exception as e:
        print("Error generating QA:", e)
        raise e

# Apply to each row and store results
questions = []
answers = []

for idx, row in df.iterrows():
    context = row['content']
    print(f"Processing row {idx + 1} of {len(df)}")
    q, a = generate_qa(context)
    questions.append(q)
    answers.append(a)
    sleep(1)  # Avoid rate limiting

# Add results to DataFrame
df['gpt_41_gs_question'] = questions
df['gpt_41_gs_answer'] = answers

# Save to output CSV
df.to_csv(output_csv, index=False)
print(f"✅ Done. Output saved to {output_csv}")
