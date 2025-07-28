import os

def count_chunks_in_folder(folder_path):
    count = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md") and file.startswith("chunk_"):
                count += 1
    return count

folder_path = os.path.abspath('./data')
total_chunks = count_chunks_in_folder(folder_path)
print(f"Total number of chunks: {total_chunks}")

