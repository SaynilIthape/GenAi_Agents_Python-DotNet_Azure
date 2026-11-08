
def chunk_text(
        text:str,
        chunk_size=500,
        overlap=100) ->list[str]:
    chunk=[]

    start=0
    if chunk_size>0 and overlap>=0 and overlap<chunk_size:
        while start < len(text):
      
            slicestr = text[start:start + chunk_size]
            chunk.append(slicestr)
            if start + chunk_size >= len(text):
                 break
            start += chunk_size-overlap
           
            
    else:
        raise ValueError("Invalid chunk configuration")
    return  chunk

def chunk_documents(
            documents:list[dict],
            chunk_size=500,
            overlap=100
            ) ->list[dict]:
    all_chunks=[]
    for document in documents:
        content = document["content"]
        metadata =  document["metadata"]
        chunks  = chunk_text(content,chunk_size,overlap)

        for index , chunk in enumerate(chunks):
            documentDict = {
                        "content":chunk,
                        "metadata":metadata.copy(),
                        "chunk_id": f"{metadata['document_id']}_{index}"
                    }
            all_chunks.append(documentDict)
    return all_chunks