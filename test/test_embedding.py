import requests

url = "http://localhost:11434/api/embed"

payload = {
     "model": "nomic-embed-text",
    "input": "Machine M100 is overheating due to low coolant flow."
}

response  = requests.post(url,json=payload, timeout=60)

response.raise_for_status()

result = response.json()

embedding = result["embeddings"][0]

print("Embedding dimensions:", len(embedding))
print("First 10 values:", embedding[:10])

