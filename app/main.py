from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from app.rag_pipeline import answer_question

class QuestionRequest(BaseModel):
    question:str = Field(
            min_length=3,
            max_length=500,
            description="Manufacturing-related question"
             )
    machine_id:str=Field(min_length=1)


app= FastAPI()

@app.post("/ask")
def ask_question(request:QuestionRequest):

    try:
        result =  answer_question(request.question,request.machine_id)

        # print("RESULT TYPE:", type(result))
        # print("RESULT:", result)
        return {
            "question": request.question,
            "answer": result["answer"],
            "sources": result["sources"]
        }
    except Exception as ex:
            print("ERROR:", repr(ex))
            raise HTTPException(
            status_code=500,
            detail="Unable to process your question."
        ) from ex

