from pathlib import Path

def load_documents() ->list[dict]:
    documents = []
    document_paths = Path("documents")

    for file_path in document_paths.rglob("*.txt"):
        content =  file_path.read_text(encoding="utf-8")
        document = {
              "content":content,
              "metadata" : {
                "document_id":get_documentId(content),
                "filename":file_path.name,
                "document_type":file_path.parent.name,
                "machine_id":file_path.name.split("_")[1]                   
              }
            }
        documents.append(document)
    return documents

def get_documentId(file_content):
     document_id = ""
     lines = file_content.splitlines()
     for line in lines:
          if line.startswith("Document ID:"):
               document_id = line.split(":",1)[1].strip()
               break;
    
     return document_id
     

# {
#     "content": "Machine temperature was recorded at 82°C...",
#     "metadata": {
#         "document_id": "DOC-M100-002",
#         "filename": "machine_M100_quality_report.txt",
#         "machine_id": "M100",
#         "part_id": "P100",
#         "document_type": "quality"
#     }
# }