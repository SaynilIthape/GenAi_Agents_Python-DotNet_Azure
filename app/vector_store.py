import chromadb


client =  chromadb.PersistentClient(path="./chroma_db")
collection  =  client.get_or_create_collection(name="manufacturing_docs",
                                metadata={"hnsw:space": "cosine"})

def store_chunk(chunks, embeddings):

   ids=[]
   documents=[]
   metadata=[]

   for chunk in chunks:
       ids.append(chunk["chunk_id"])
       documents.append(chunk["content"])
       metadata.append(chunk["metadata"])

   collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadata
    )
   return len(ids)