import requests

# url = "http://localhost:11434/api/embed"

def generate_embeddings(chunks):
     url = "http://localhost:11434/api/embed"

     payload = {
        "model": "nomic-embed-text",
        "input": [chunk["content"] for chunk in chunks]
      }
     response  = requests.post(url,json=payload, timeout=60)

     response.raise_for_status()

     result = response.json()

     embedding = result["embeddings"]
     return embedding