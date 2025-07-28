import os
import pandas as pd

# Root chunks folder (where all chunk subfolders live)
chunks_root = os.path.abspath('./data/chunks')

# Store all chunk rows
data = []

# Loop through each subfolder inside chunks/
for folder_name in sorted(os.listdir(chunks_root)):
    folder_path = os.path.join(chunks_root, folder_name)
    
    if os.path.isdir(folder_path):
        for idx, filename in enumerate(sorted(os.listdir(folder_path))):
            if filename.endswith('.md'):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    base_name = os.path.splitext(filename)[0]
                    chunk_id = f"{folder_name}_{base_name}"
                    full_filename = f"{folder_name}/{filename}"
                    
                    data.append({
                        'chunk_id': chunk_id,
                        'filename': full_filename,
                        'content': content
                    })

# Save to CSV
df = pd.DataFrame(data)
output_csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'all_chunks.csv')
df.to_csv(output_csv_path, index=False)

print(f"✅ Saved {len(df)} chunks from all folders to {output_csv_path}.")
