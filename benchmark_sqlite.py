import sqlite3
import time
import os

db_path = "benchmark.db"
if os.path.exists(db_path):
    os.remove(db_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE conversation_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT,
        content TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Insert 10,000 records
print("Inserting 10,000 records...")
data = [("user", f"message {i}") for i in range(10000)]
cursor.executemany('INSERT INTO conversation_history (role, content) VALUES (?, ?)', data)
conn.commit()

def benchmark_query(order_by, iterations=1000):
    start_time = time.time()
    for _ in range(iterations):
        cursor.execute(f'SELECT role, content FROM conversation_history ORDER BY {order_by} LIMIT 10')
        cursor.fetchall()
    end_time = time.time()
    return end_time - start_time

print("Benchmarking...")
ts_time = benchmark_query("timestamp DESC")
id_time = benchmark_query("id DESC")

print(f"ORDER BY timestamp DESC: {ts_time:.4f}s")
print(f"ORDER BY id DESC: {id_time:.4f}s")
print(f"Speedup: {ts_time / id_time:.2f}x")

conn.close()
os.remove(db_path)
