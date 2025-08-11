from app.retriever import Retriever
from app.router import pick_domain

r = Retriever()

queries = [
    "Fever and cough treatment at home",
    "Pastel summer outfit ideas",
    "Which shoes match with a floral dress?",
    "Symptoms of type 2 diabetes"
]

for q in queries:
    domain, info = pick_domain(q, r)
    print(f"\nQuery: {q}")
    print(f"Chosen domain: {domain}")
    print(f"Scores: {info['domain_score']}")
    print("Top hits:")
    for hit in info["hits"]:
        print(f" - {hit['doc']} ({hit['score']:.3f})")
