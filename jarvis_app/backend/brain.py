import json
import requests
from memory import MemoryManager

class Brain:
    def __init__(self, db_path="jarvis_memory.db", llm_url="http://localhost:11434/api/generate"):
        self.memory = MemoryManager(db_path)
        self.llm_url = llm_url
        # Optimization: Use requests.Session to reuse TCP connections, reducing latency
        self.session = requests.Session()

    def store_memory(self, key, value):
        # Using a simple key-value store for now, can be extended to memory table
        return f"Stored {key} in memory"

    def add_to_history(self, role, content):
        self.memory.add_conversation(role, content)

    def get_history(self, limit=10):
        return self.memory.get_recent_history(limit)

    def think(self, user_input):
        # Prepare context from memory and history
        history = self.get_history()
        history_str = "\n".join([f"{h[0]}: {h[1]}" for h in history])

        system_prompt = """You are Jarvis, a highly capable AI assistant.
        You have control over the user's computer.
        You can move the mouse, type, and open applications.
        If the user asks for a system action, respond with a JSON object in this format:
        {"action": "move_mouse", "params": {"x": 100, "y": 200}}
        Available actions: move_mouse, click, type, press, open_whatsapp, open_mt5, browse (params: {"url": "https://example.com"}).
        If it's just a conversation, just reply normally.
        Always be helpful and polite."""

        prompt = f"{system_prompt}\n\nRecent History:\n{history_str}\nUser: {user_input}\nJarvis:"

        try:
            # Assuming Ollama is running locally
            # Optimization: Use self.session to reuse TCP connections
            response = self.session.post(self.llm_url, json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }, timeout=30)

            if response.status_code == 200:
                ai_reply = response.json().get("response", "").strip()
                self.add_to_history("user", user_input)
                self.add_to_history("jarvis", ai_reply)
                return ai_reply
            else:
                return "I'm having trouble thinking right now. Is Ollama running?"
        except Exception as e:
            # Fallback if LLM is not available
            return f"I can't access my brain right now. Error: {str(e)}. Please make sure Ollama is installed and running."

    def parse_action(self, ai_reply):
        try:
            # Try to find JSON in the response
            import re
            json_match = re.search(r'\{.*\}', ai_reply, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass
        return None
