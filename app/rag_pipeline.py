from app.retrieval import retrival_document
from app.generation import generate_response

def answer_question(question:str,machine_id:str):
    results =  retrival_document(question,machine_id)

    sources=[]
    for i, metadata in enumerate(results["metadatas"][0]):
        sources.append({
                 "document_id": metadata["document_id"],
                 "filename": metadata["filename"],
                 "chunk_id": results["ids"][0][i],
                 "distance": results["distances"][0][i]
        })

    documents= results["documents"][0]

    context = "\n\n".join(documents)

    prompt = f"""
             You are a manufacturing maintenance assistant.

            Answer the question using ONLY the context provided.

            If the context does not contain sufficient information,
            clearly say that the available documents do not contain
            sufficient information.
            Context:{context}
            Question :{question}
            Answer:
            """
    # print("Retrieved context:")
    # print(context)
    answer = generate_response(prompt)


    FALLBACK_RESPONSE = (
    "The available manufacturing documents do not "
    "contain sufficient information to answer this question."
    )

    if not results["documents"][0]:
        return  {
        "answer": FALLBACK_RESPONSE,
        "sources": []
        }
    else:
          return  {
                "answer": answer,
                "sources": sources
                }