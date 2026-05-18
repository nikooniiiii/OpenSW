from fastapi import APIRouter, Form
import requests

router = APIRouter()

@router.post("/ask")
async def ask_llm(prompt: str = Form(...)):
  
    url = "http://localhost:11434/api/generate"
    
    data = {
        "model": "qwen2.5-coder:0.5b",
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data)
      
        if response.status_code != 200:
            return {
                "message": "LLM сервертэй холбогдоход алдаа гарлаа",
                "status_code": response.status_code
            }
        
        result = response.json()
        
        return {
            "prompt": prompt,
            "answer": result["response"]
        }
        
    except Exception as e:
        return {"error": str(e)}