from app.ingestion import load_documents
documents =  load_documents()
print(f"Total documents:  {len(documents)}")

for doc in documents:
    print(doc)
