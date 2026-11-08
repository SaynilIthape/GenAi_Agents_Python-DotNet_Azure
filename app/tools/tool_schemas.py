
machine_tools = [{
    "type":"functions",
    "function":{
            "name":"get_machine_status",
            "description":"Get the current status and temperature of a manufacturing machine.",
            "parameters":{
                 "type": "object",
                 "properties": {
                    "machine_id": {
                        "type": "string",
                        "description": "Unique machine identifier, e.g. M100"
                    }
                },
                "required": ["machine_id"]
            }
        }
    },
    {
        "type":"functions",
        "function":{
                    "name":"search_maintenance_documents",
                    "description":"Search maintenance documents for troubleshooting procedures and recommendations.",
                    "parameters": {
                         "type": "object",
                         "properties": {
                              "question": {
                                    "type": "string",
                                    "description": "Maintenance-related question"
                                },
                              "machine_id": {
                                    "type": "string",
                                    "description": "Machine identifier, e.g. M100"
                                }
                        },
                        "required": ["question"]
                    }
            }
    }   
]