# build_index.py
import os, glob, pickle
from pathlib import Path
import numpy as np
from sentence_transformers import SentenceTransformer

CHUNK_SIZE = 600
CHUNK_OVERLAP = 100

DOMAINS = {
    "healthcare": "data/healthcare",
    "fashion": "data/fashion",
}

OUT_DIR = Path("indices")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def read_txts(folder):
    items = []
    for path in glob.glob(os.path.join(folder, "*.txt")):
        with open(path, "r", encoding="utf-8") as f:
            items.append((os.path.basename(path), f.read()))
    return items

def chunk_text(text, size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    chunks = []
    i = 0
    n = len(text)
    step = max(1, size - overlap)
    while i < n:
        chunks.append(text[i:i+size])
        i += step
    return [c.strip() for c in chunks if c.strip()]

def build_for_domain(domain, folder, model):
    meta = []   # [{id, doc, chunk, text}]
    uid = 0
    for docname, full in read_txts(folder):
        for ci, chunk in enumerate(chunk_text(full)):
            meta.append({
                "id": f"{domain}-{uid}",
                "doc": docname,
                "chunk": ci,
                "text": chunk
            })
            uid += 1
    if not meta:
        print(f"[WARN] No .txt found for domain={domain} in {folder}")
        vecs = np.zeros((0, 384), dtype=np.float32)
    else:
        corpus = [m["text"] for m in meta]
        vecs = model.encode(corpus, convert_to_numpy=True, normalize_embeddings=True)
    np.save(OUT_DIR / f"{domain}_vecs.npy", vecs)
    with open(OUT_DIR / f"{domain}_meta.pkl", "wb") as f:
        pickle.dump(meta, f)
    dim = 0 if vecs.shape[0]==0 else vecs.shape[1]
    print(f"[OK] {domain}: {len(meta)} chunks, dim={dim}")

def main():
    # Türkçe + çok dilli iyi giderse bunu da düşünebilirsin:
    # model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    model = SentenceTransformer(model_name)
    for domain, folder in DOMAINS.items():
        build_for_domain(domain, folder, model)

if __name__ == "__main__":
    main()
