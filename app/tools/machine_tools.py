
def get_machine_status(machine_id:str):
    machine= {
        "M100":{
                "status": "Running",
            "temperature": 95,
            "health": "Warning"
        },
         "M200": {
            "status": "Stopped",
            "temperature": 30,
            "health": "Normal"
        }
    }
    return machine.get(machine_id,"machine not found")

from app.rag_pipeline import answer_question

def search_maintenance_documents(
                    question:str, 
                    machine_id:str=None):

    return answer_question(question,machine_id)