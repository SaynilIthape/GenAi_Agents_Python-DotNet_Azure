from app.chunking import chunk_text
from app.ingestion import load_documents

documents = load_documents()
chunks = chunk_text(
    documents,
    chunk_size=500,
    overlap=100
)

print(f"Total documents: {len(documents)}")
print(f"Total chunks: {len(chunks)}")

for chunk in chunks:
    print(chunk)