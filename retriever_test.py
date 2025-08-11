from app.retriever import Retriever

r = Retriever()

query1 = "Fever and cough, what should I do?"
print("\nHealthcare results:")
for res in r.search_domain("healthcare", query1, k=2):
    print(res["score"], res["doc"], "→", res["text"][:60])

query2 = "pastel summer outfit"
print("\nFashion results:")
for res in r.search_domain("fashion", query2, k=2):
    print(res["score"], res["doc"], "→", res["text"][:60])
