import sqlite3
import json
from datetime import datetime
import os

class MemoryManager:
    def __init__(self, db_path="jarvis_memory.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # 1. Trade Log
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS trade_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                symbol TEXT,
                direction TEXT,
                entry_price REAL,
                exit_price REAL,
                pnl REAL,
                regime TEXT,
                confidence REAL,
                status TEXT
            )
        ''')

        # 2. Signal Performance
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS signal_performance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                signal_name TEXT,
                regime TEXT,
                win_rate REAL,
                total_trades INTEGER,
                last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # 3. Regime History
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS regime_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                regime TEXT,
                duration_hours REAL,
                avg_volatility REAL
            )
        ''')

        # 4. Model Performance
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS model_performance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                model_name TEXT,
                accuracy REAL,
                precision REAL,
                recall REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # 5. Market Events
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS market_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type TEXT,
                impact TEXT,
                description TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Conversation history (inherited from previous version)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversation_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT,
                content TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Optimize trade_log queries with an index on status
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_trade_log_status ON trade_log (status)')

        conn.commit()
        conn.close()

    def log_trade(self, symbol, direction, entry_price, regime, confidence):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO trade_log (symbol, direction, entry_price, regime, confidence, status)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (symbol, direction, entry_price, regime, confidence, 'OPEN'))
        conn.commit()
        trade_id = cursor.lastrowid
        conn.close()
        return trade_id

    def add_conversation(self, role, content):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO conversation_history (role, content) VALUES (?, ?)', (role, content))
        conn.commit()
        conn.close()

    def get_recent_history(self, limit=10):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # Optimized: Sorting by INTEGER PRIMARY KEY (id) is significantly faster than DATETIME (timestamp)
        # in SQLite as it leverages the automatic primary key index.
        cursor.execute('SELECT role, content FROM conversation_history ORDER BY id DESC LIMIT ?', (limit,))
        history = cursor.fetchall()
        conn.close()
        return history[::-1]

    def get_stats(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM trade_log')
        total_trades = cursor.fetchone()[0]
        cursor.execute('SELECT AVG(pnl) FROM trade_log WHERE status="CLOSED"')
        avg_pnl = cursor.fetchone()[0] or 0.0
        conn.close()
        return {"total_trades": total_trades, "avg_pnl": avg_pnl}
