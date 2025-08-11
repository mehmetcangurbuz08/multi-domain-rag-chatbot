# retriever.py
import numpy as np
import pickle
from pathlib import Path
from typing import List, Dict
from sentence_transformers import SentenceTransformer

INDICES_DIR = Path("indices")

class DomainRetriever:
    def __init__(self, domain: str, model: SentenceTransformer):
        self.domain = domain
        self.model = model

        # Vektörleri ve meta veriyi yükle
        self.vecs = np.load(INDICES_DIR / f"{domain}_vecs.npy")
        with open(INDICES_DIR / f"{domain}_meta.pkl", "rb") as f:
            self.meta = pickle.load(f)

    def search(self, query: str, k: int = 3) -> List[Dict]:
        """Verilen query için top-k en benzer chunkları döndürür."""
        if self.vecs.shape[0] == 0:
            return []

        # Sorguyu embed et
        q_vec = self.model.encode([query], convert_to_numpy=True, normalize_embeddings=True)[0]

        # Cosine similarity (normalize edildiği için dot product = cosine)
        scores = self.vecs @ q_vec

        # En yüksek skorları bul
        topk_idx = np.argsort(-scores)[:k]

        results = []
        for idx in topk_idx:
            results.append({
                "score": float(scores[idx]),
                "id": self.meta[idx]["id"],
                "doc": self.meta[idx]["doc"],
                "chunk": self.meta[idx]["chunk"],
                "text": self.meta[idx]["text"],
            })
        return results


class Retriever:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.domains = {
            "healthcare": DomainRetriever("healthcare", self.model),
            "fashion": DomainRetriever("fashion", self.model)
        }

    def search_domain(self, domain: str, query: str, k: int = 3) -> List[Dict]:
        return self.domains[domain].search(query, k)

    def search_all(self, query: str, k: int = 3) -> Dict[str, List[Dict]]:
        return {d: retr.search(query, k) for d, retr in self.domains.items()}
