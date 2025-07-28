import os
from openai import AzureOpenAI
import pandas as pd
from time import sleep
import re

# Initialize OpenAI client
client = AzureOpenAI(
    api_key= "55a6f00f-0e01-4a39-85de-3bb90460d96f",
    azure_endpoint = "https://api.nlp.p.uptimize.merckgroup.com",
    api_version="2024-10-21" # Pass Based on Model Version
)

# File paths
input_csv = os.path.abspath('./questions_with_text.csv')
df = pd.read_csv(input_csv, encoding='latin1')

results = []

def extract_choice_and_answer(reply):
    lines = reply.split('\n')
    choice = next((line[2:].strip() for line in lines if line.strip().lower().startswith("c:")), "Unknown")
    answer = next((line[2:].strip() for line in lines if line.strip().lower().startswith("a:")), reply)
    return choice, answer


for idx, row in df.iterrows():
    context = row['content']
    qA = row['questionA']
    qB = row['questionB']
    qa_id = row['QA_id']

    prompt = f"""You will read each time two questions and one context (chunk of BayBE documentation).
Each question may have been written by either a human or an LLM, and both questions are asking for information from the context.
Which question is more 'human-like'? Please answer "A" or "B" and give the reason for your choice.

Context:
{context}

Question A:
{qA}

Question B:
{qB}

return:
C: <A or B>
A: <answer>

"""

    print(f"Sending prompt for QA_id: {qa_id}")
    try:
        response = client.chat.completions.create(
            model="gpt-41-gs", 
            messages=[
                {"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=300
        )
        print(f"Received response for QA_id: {qa_id}")
        reply = response.choices[0].message.content

        lines = reply.split("\n")
        lines = reply.split('\n')
        choice = next((line[2:].strip() for line in lines if line.strip().lower().startswith("c:")), "Unknown")
        answer = next((line[2:].strip() for line in lines if line.strip().lower().startswith("a:")), reply)
        results.append({'QA_id': qa_id, 'answer': choice, 'reason': answer})
    except Exception as e:
        print(f"Error for QA_id {qa_id}: {e}")
        results.append({'QA_id': qa_id, 'answer': 'Error', 'reason': str(e)})

    sleep(1.2)  # Adjust as needed to avoid rate limits

# Save to new CSV
results_df = pd.DataFrame(results)
results_df.to_csv('humanlike_judgment.csv', index=False)