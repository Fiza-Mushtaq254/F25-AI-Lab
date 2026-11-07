from lab6_chunks import documents, sentence_chunks
from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer
records = []
for doc_id, text in documents.items():
    chunks = sentence_chunks(text, size=40, doc_id=doc_id)
    for chunk in chunks:
        records.append({
            "id": chunk["id"],
            "start": chunk["start"],
            "end": chunk["end"],
            "text": chunk["text"]
        })
texts = [record["text"] for record in records]
queries = [
    "Is there any special rule for students who cannot meet a deadline?",
    "How do students access library resources?",
    "How can students deal with transport delays on campus?"
]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(texts)
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    device="cpu"
)
embedding_matrix = model.encode(
    texts,
    normalize_embeddings=True
)
print("TF-IDF and Embedding Results")
for query in queries:
    print("\nQuery:", query)
    tfidf_query = vectorizer.transform([query])
    tfidf_scores = (tfidf_query @ tfidf_matrix.T).toarray()[0]
    embedding_query = model.encode(
        [query],
        normalize_embeddings=True
    )[0]
    embedding_scores = embedding_matrix @ embedding_query
    for name, scores in [
        ("TF-IDF", tfidf_scores),
        ("Embedding", embedding_scores)
    ]:
        print("\n", name)
        ranked = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )
        for i in ranked[:3]:
            print("Chunk ID:", records[i]["id"])
            print("Score:", round(float(scores[i]), 3))
            print("Evidence:", records[i]["text"])
