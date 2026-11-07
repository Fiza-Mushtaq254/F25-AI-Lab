from lab6_chunks import documents, sentence_chunks
from sentence_transformers import SentenceTransformer
records = []
for doc_id, text in documents.items():
    chunks = sentence_chunks(text, size=40, doc_id=doc_id)
    for chunk in chunks:
        records.append({
            "id": chunk["id"],
            "text": chunk["text"]
        })
texts = [record["text"] for record in records]
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    device="cpu"
)
embeddings = model.encode(
    texts,
    normalize_embeddings=True
)
query = "What should students do when they need help with university services?"
query_embedding = model.encode(
    [query],
    normalize_embeddings=True
)[0]
scores = embeddings @ query_embedding
ranked = sorted(
    range(len(scores)),
    key=lambda i: scores[i],
    reverse=True
)
print("Query:", query)
print("\nSuggested Results:")
for i in ranked[:3]:
    print("\nSuggestion:", records[i]["text"])
    print("Chunk ID:", records[i]["id"])
    print("Score:", round(float(scores[i]), 3))