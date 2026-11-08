from app.embeddings import generate_embeddings
from app.ingestion import load_documents
from app.chunking import chunk_documents
from app.vector_store import store_chunk
from app.vector_store import collection


documents = load_documents()
# print("First document:")
# print(documents[0])

# print("Metadata:")
# print(documents[0]["metadata"])

# print("Metadata keys:")
# print(documents[0]["metadata"].keys())

chunks = chunk_documents(documents)

embeddings = generate_embeddings(chunks)

count = store_chunk(chunks, embeddings)

result=collection.get(include=["documents", "metadatas", "embeddings"])

print(result)

for i in range(len(result["ids"])):
    print("ID:", result["ids"][i])
    print("Document:", result["documents"][i][:100])
    print("Metadata:", result["metadatas"][i])
    print("----------------------")

print(f"Stored {count} chunks in ChromaDB")