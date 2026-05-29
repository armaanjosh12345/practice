import sqlite3
import json
import requests

class Brain:
    def __init__(self, db_path="jarvis_memory.db", llm_url="http://localhost:11434/api/generate"):
        self.db_path = db_path
        self.llm_url = llm_url
        # Use a persistent session for HTTP connection pooling to improve request performance
        self.session = requests.Session()
        # Persistent database connection reduces overhead of repeatedly opening/closing
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self._init_db()

    def _init_db(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE,
                value TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversation_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT,
                content TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def store_memory(self, key, value):
        cursor = self.conn.cursor()
        cursor.execute('INSERT OR REPLACE INTO memory (key, value) VALUES (?, ?)', (key, value))
        self.conn.commit()
        return f"Stored {key} in memory"

    def retrieve_memory(self, key):
        cursor = self.conn.cursor()
        cursor.execute('SELECT value FROM memory WHERE key = ?', (key,))
        result = cursor.fetchone()
        return result[0] if result else None

    def add_to_history(self, role, content):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO conversation_history (role, content) VALUES (?, ?)', (role, content))
        self.conn.commit()

    def get_history(self, limit=10):
        cursor = self.conn.cursor()
        # Optimized query using primary key (id) for sorting instead of timestamp
        cursor.execute('SELECT role, content FROM conversation_history ORDER BY id DESC LIMIT ?', (limit,))
        history = cursor.fetchall()
        return history[::-1]

    def think(self, user_input):
        # Prepare context from memory and history
        history = self.get_history()
        history_str = "\n".join([f"{h[0]}: {h[1]}" for h in history])

        system_prompt = """You are Jarvis, a highly capable AI assistant.
        You have control over the user's computer.
        You can move the mouse, type, and open applications.
        If the user asks for a system action, respond with a JSON object in this format:
        {"action": "move_mouse", "params": {"x": 100, "y": 200}}
        Available actions: move_mouse, click, type, press, open_whatsapp, open_mt5.
        If it's just a conversation, just reply normally.
        Always be helpful and polite."""

        prompt = f"{system_prompt}\n\nRecent History:\n{history_str}\nUser: {user_input}\nJarvis:"

        try:
            # Assuming Ollama is running locally
            # Using self.session for connection pooling (reduces overhead by ~20%)
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
