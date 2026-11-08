import requests

def generate_response(prompt:str) -> str:
     url = "http://localhost:11434/api/generate"
    
     payload = {
            "model": "llama3.2:3b",
            "prompt": prompt,
            "stream": False
          }
     response  = requests.post(url,json=payload, timeout=60)
    
     response.raise_for_status()
    
     result = response.json()
     return result["response"]