import requests
import chromadb


client =  chromadb.PersistentClient(path="./chroma_db")
collection  =  client.get_or_create_collection(name="manufacturing_docs",
                                metadata={"hnsw:space": "cosine"})

def retrival_document(questions:str, machine_id:str=None):
        query_embedding = generate_query_embedding(questions)

        where_filter = None
        if machine_id:
                where_filter={
                     "machine_id": machine_id
                }
        result = collection.query(query_embeddings=[query_embedding],
                                  n_results=3,
                                  where=where_filter,
                                  include=["documents", "metadatas", "distances"])
        return result


def generate_query_embedding(question: str) -> list[float]:
         url = "http://localhost:11434/api/embed"    
         payload = {
            "model": "nomic-embed-text",
            "input": question
          }
         response  = requests.post(url,json=payload, timeout=60)
    
         response.raise_for_status()
    
         result = response.json()
    
         embedding = result["embeddings"][0]
         return embedding