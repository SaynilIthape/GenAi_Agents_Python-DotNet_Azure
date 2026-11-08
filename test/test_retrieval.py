from app.retrieval import retrival_document

question = "Why is machine M100 overheating?"
results =  retrival_document(question,top_k=3)

for i , document in enumerate(results["documents"][0]):
    print(f"\nResult{i+1}")
    print("Document",document)
    print("Metadata:", results["metadatas"][0][i])
    print("Distance:", results["distances"][0][i])