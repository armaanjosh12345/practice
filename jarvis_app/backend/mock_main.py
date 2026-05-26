from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"status": "Jarvis Mock Backend is running"}

@app.post("/chat")
async def chat(message: Message):
    text = message.text.lower()

    if "open whatsapp" in text:
        reply = 'Certainly, sir. Opening WhatsApp for you now. {"action": "open_whatsapp", "params": {}}'
        execution_result = "Opening WhatsApp"
    elif "status" in text or "system" in text:
        reply = "Systems are nominal. CPU is at 15%, Memory usage is 42%. Battery is healthy at 88%."
        execution_result = None
    elif "hello" in text or "hi" in text:
        reply = "Hello sir. Ready to assist with your Precision 5550."
        execution_result = None
    else:
        reply = "I've processed your request, sir. Is there anything else?"
        execution_result = None

    return {
        "reply": reply,
        "action": None, # Simulation simplifies this
        "execution_result": execution_result
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
