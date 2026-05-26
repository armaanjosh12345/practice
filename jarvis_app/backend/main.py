from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .brain import Brain
from .system_controller import SystemController
import uvicorn

app = FastAPI()
brain = Brain()
controller = SystemController()

class Message(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"status": "Jarvis Backend is running"}

@app.post("/chat")
async def chat(message: Message):
    try:
        # 1. AI thinks
        reply = brain.think(message.text)

        # 2. Check if there's a system action
        action_data = brain.parse_action(reply)

        execution_result = None
        if action_data:
            action = action_data.get("action")
            params = action_data.get("params", {})
            # 3. Execute action
            execution_result = controller.execute_command(action, params)

        return {
            "reply": reply,
            "action": action_data,
            "execution_result": execution_result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
