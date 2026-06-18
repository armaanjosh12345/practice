from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from brain import Brain
from system_controller import SystemController
from system_info import get_system_stats
from data_collector import DataCollector
from trading_bridge import TradingBridge
from memory import MemoryManager
import uvicorn

app = FastAPI()
brain = Brain()
controller = SystemController()
data_collector = DataCollector()
trading_bridge = TradingBridge()
memory = MemoryManager()

class Message(BaseModel):
    text: str

@app.get("/")
def root():
    # Changed from async def to def to allow FastAPI to run this in a thread pool.
    # This prevents blocking the event loop during synchronous system stat gathering and DB calls.
    stats = get_system_stats()
    trading_stats = memory.get_stats()
    return {
        "status": "Jarvis Quantum Sandbox Backend is running",
        "system": stats,
        "trading": trading_stats
    }

@app.post("/chat")
def chat(message: Message):
    # Changed from async def to def to allow FastAPI to run this in a thread pool.
    # This prevents blocking the event loop during high-latency synchronous LLM requests.
    try:
        # Get system context
        stats = get_system_stats()
        context_msg = f" [System Context: CPU {stats['cpu_usage']}, RAM {stats['memory_usage']}, Battery {stats['battery']}]"

        # 1. AI thinks with system context
        reply = brain.think(message.text + context_msg)

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
