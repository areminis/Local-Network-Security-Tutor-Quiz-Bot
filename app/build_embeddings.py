import os, re, pdfplumber
from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="embeddings")
collection = client.get_or_create_collection("network_security")

def extract_text(path):
    """Extract clean text from PDF or TXT with layout cleanup."""
    text = ""
    if path.endswith(".pdf"):
        with pdfplumber.open(path) as pdf:
            for p in pdf.pages:
                t = p.extract_text() or ""
                t = re.sub(r"•|·|▪|▶|►|–|-", " ", t)  # remove bullet symbols
                t = re.sub(r"\s{2,}", " ", t)         # collapse spaces
                t = re.sub(r"Page\s*\d+", "", t)      # remove page labels
                text += " " + t
    else:
        with open(path, encoding="utf-8", errors="ignore") as f:
            text = f.read()

    # remove figure captions, lecture titles, slide headers
    text = re.sub(r"Figure\s*\d+.*", "", text)
    text = re.sub(r"Lecture\s*\d+.*", "", text)
    text = re.sub(r"Outline.*", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def chunk_text(text, size=120):
    """Split clean text into smaller sentences or topic chunks."""
    sentences = re.split(r'(?<=[.?!])\s+', text)
    chunks, current = [], []
    count = 0
    for s in sentences:
        current.append(s)
        count += len(s.split())
        if count > size:
            chunks.append(" ".join(current))
            current, count = [], 0
    if current:
        chunks.append(" ".join(current))
    return chunks

def embed_folder(folder, source_type):
    if not os.path.exists(folder):
        print(f"⚠️ Folder not found: {folder}")
        return
    for file in os.listdir(folder):
        fpath = os.path.join(folder, file)
        if not os.path.isfile(fpath): continue
        print(f"🔹 Embedding from: {source_type}/{file}")
        text = extract_text(fpath)
        chunks = chunk_text(text)
        for i, chunk in enumerate(chunks):
            collection.add(
                documents=[chunk],
                ids=[f"{source_type}_{file}_{i}"],
                metadatas=[{"source_type": source_type, "filename": file}]
            )
    print(f"✅ Embedded all from {source_type}")

if __name__ == "__main__":
    embed_folder("data/Lectures", "lecture_slide")
    embed_folder("data/Lectures_text", "lecture_slide_Formatted")
    embed_folder("data/textbooks", "textbook")
    embed_folder("data/internet_sources", "internet_source")
    embed_folder("data/Assignments", "assignment")
    embed_folder("data/Quizzes", "quiz")
    print("🎉 All data embedded successfully!")
    print("📊 Total documents:", collection.count())
