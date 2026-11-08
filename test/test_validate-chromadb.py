import chromadb

client =  chromadb.PersistentClient(path="./chroma_db")

collection =  client.get_or_create_collection(name="manufacturing_docs",
                                metadata={"hnsw:space": "cosine"})
print(client.list_collections())
print(collection.peek())
# result =  collection.get(ids=["DOC-M100-001_0"],
#                          include=["documents", "metadatas","embeddings"])

# print(result)