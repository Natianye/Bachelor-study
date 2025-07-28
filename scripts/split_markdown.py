import os

def split_markdown_with_context(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    chunks = []
    current_chunk = []
    h1 = None  # First-level header
    h2 = None  # Second-level header
    first_h1_found = False
    started_chunk_after_h1 = False  # Prevent adding h1-only chunks

    def save_chunk():
        nonlocal current_chunk, started_chunk_after_h1
        if current_chunk and any(line.strip() for line in current_chunk):
            chunks.append('\n'.join(current_chunk).strip())
            started_chunk_after_h1 = True
        current_chunk = []

    for line in lines:
        line_strip = line.strip()

        # Skip everything before the first h1
        if not first_h1_found:
            if line_strip.startswith('# '):
                first_h1_found = True
                h1 = line_strip
            continue

        # Ignore additional top-level headers (treat as content)
        if line_strip.startswith('# '):
            current_chunk.append(line.rstrip())

        elif line_strip.startswith('## '):
            save_chunk()
            h2 = line_strip
            current_chunk = []
            if h1:
                current_chunk.append(h1)
            current_chunk.append(h2)

        elif line_strip.startswith('### '):
            save_chunk()
            current_chunk = []
            if h1:
                current_chunk.append(h1)
            if h2:
                current_chunk.append(h2)
            current_chunk.append(line_strip)

        else:
            if not started_chunk_after_h1 and h1 and not current_chunk:
                # Delay h1 chunk creation until content appears
                current_chunk.append(h1)
            if h2 and not current_chunk:
                current_chunk.append(h2)
            current_chunk.append(line.rstrip())

    save_chunk()
    return chunks


def save_chunks(base_output_dir, folder_path, filepath, chunks):
    # Get relative path to keep folder structure
    rel_path = os.path.relpath(filepath, folder_path)
    rel_base = os.path.splitext(rel_path)[0]
    # Replace path separators to create safe folder name
    safe_subdir = rel_base.replace(os.sep, "_") + "_chunks"

    base_dir = os.path.join(base_output_dir, safe_subdir)
    os.makedirs(base_dir, exist_ok=True)

    for i, chunk in enumerate(chunks):
        chunk_path = os.path.join(base_dir, f"chunk_{i+1}.md")
        with open(chunk_path, 'w', encoding='utf-8') as f:
            f.write(chunk)

def process_folder(folder_path, output_path):
    all_chunks = {}
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.md'):
                file_path = os.path.join(root, filename)
                chunks = split_markdown_with_context(file_path)
                all_chunks[file_path] = chunks
                save_chunks(output_path, folder_path, file_path, chunks)
    return all_chunks

folder_path = os.path.abspath('./markdown')
output_path = os.path.abspath('./data/chunks')

chunks_dict = process_folder(folder_path, output_path)
