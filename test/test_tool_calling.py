from app.tools.tool_schemas import machine_tools
from app.tools.machine_tools import get_machine_status, search_maintenance_documents
import requests
import json

available_functions = {
    "get_machine_status": get_machine_status,
    "search_maintenance_documents": search_maintenance_documents
}


url = "http://localhost:11434/api/chat"

payload = {
     "model": "llama3.2:3b",
     "messages":[{
        "role": "user",
        "content": "Why is machine M100 showing high temperature, and what maintenance procedure should I follow?"
     }],
     "tools":machine_tools,
     "stream": False
    }

response =  requests.post(url,json=payload,timeout=60)
# print("STATUS:", response.status_code)
# print("ERROR:", response.text)
response.raise_for_status()
result= response.json()


# print("result:",result["message"])
max_iterations = 3
for iteration in range(max_iterations):

    message =  result["message"]

    # Check whether LLM requested a tool
    if not message.get("tool_calls"):
        print("Final answer:", message["content"])
        break

    # presever tool call message
    payload["messages"].append(message)

    # print(payload["messages"])
    # if message.get("tool_calls"):
    for tool_call in message["tool_calls"]:
            function_name =  tool_call["function"]["name"]
            function_arg = tool_call["function"]["arguments"]

            available_function = available_functions.get(function_name)
            if  available_function:
                tool_result =  available_function(**function_arg)
                print("Tool result:", tool_result)
            else:
                tool_result = "Unknown tool"
            # Send tool result back to Ollama

            #  print(payload["messages"])
            payload["messages"].append(
                    {
                        "role":"tool",
                        "tool_name": function_name,
                        "content": json.dumps(tool_result)
                    }
                )

                
    # print("2:",payload["messages"])
    ollamaRes=  requests.post(url,json=payload,timeout=60)
    ollamaRes.raise_for_status()
    final_result = ollamaRes.json()
    # print("Final answer:", final_result["message"]["content"])
