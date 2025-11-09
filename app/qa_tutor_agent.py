import re, random, subprocess
from sentence_transformers import SentenceTransformer
import chromadb
import os, subprocess

# ----------------------------
# Load Embedding Model + DB
# ----------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="embeddings")
collection = client.get_or_create_collection("network_security")

# ----------------------------
# Helper: Query local Ollama Llama-3.2-3B
# ----------------------------
'''def run_llama(prompt, model_name="mistral"):
#def run_llama(prompt, model_name="llama3.2:3b"):
    """Runs prompt through local Ollama model (offline)."""
# Set this path manually based on "where ollama"'''
OLLAMA_PATH = r"C:\Users\alekh\AppData\Local\Programs\Ollama\ollama.exe"

def run_llama(prompt, model_name="llama3.2:3b"):
    """Runs prompt through local Ollama model (offline)."""
    try:
        result = subprocess.run(
            [OLLAMA_PATH, "run", model_name],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=120
        )
        
        output = result.stdout.decode("utf-8").strip()
        if not output:
            return f"⚠️ No response from Llama model.\nError: {result.stderr.decode('utf-8')}"
        return output
    except Exception as e:
        return f"⚠️ Llama model error: {e}"

# ----------------------------
# Helper: Clean retrieved text
# ----------------------------
def clean_text(text):
    text = re.sub(r"Figure\s*\d+(\.\d+)?|Table\s*\d+(\.\d+)?", "", text, flags=re.IGNORECASE)
    text = re.sub(r"Page\s*\d+|Slide\s*\d+", "", text, flags=re.IGNORECASE)
    text = re.sub(r"References?:.*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"[\r\n\t]+", " ", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()

# ----------------------------
# Tutor main logic
# ----------------------------
def ask(question, top_k=3):
    """Retrieves local context from Chroma and uses Llama-3.2 to generate a clear answer."""
    q_emb = model.encode(question).tolist()
    results = collection.query(query_embeddings=[q_emb], n_results=top_k)

    if not results["documents"] or not results["documents"][0]:
        return (
            "⚠️ No relevant content found in local data. Please ask a course-related question.",
            "system"
        )

    docs, metas = results["documents"][0], results["metadatas"][0]
    cleaned = [clean_text(d) for d in docs if len(d.split()) > 8]
    if not cleaned:
        return ("⚠️ Retrieved content too short to answer.", "system")

    context = "\n\n".join(cleaned[:3])

    # Build structured prompt for local Llama
    prompt = f"""
You are a helpful Network Security Tutor.
Use ONLY the context below to answer the question in some clear bullet points use only . bullets.
If formulas appear, include them in simple readable form.
Avoid figure numbers, page labels, or unrelated noise.

Context:
{context[:200]}
Question: {question}

Answer:
"""

    # Generate answer via local Llama
    answer = run_llama(prompt)

    # Collect sources
    srcs = sorted({f"{m.get('source_type','?')} → {m.get('filename','?')}" for m in metas})
    src_line = "\n".join(srcs)

    # Clean output
    answer = re.sub(r"\n{3,}", "\n\n", answer.strip())
    return f"{answer}\n\n📚 Sources:\n{src_line}", src_line

# 🧩 Quick local test
if __name__ == "__main__":
    while True:
        q = input("\nAsk a question (or type 'exit'): ")
        if q.lower() == "exit":
            break
        ans, src = ask(q)
        print("\n🧠 Answer:\n", ans)
        #print("\n📚 Sources:\n", src)