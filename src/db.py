import time
import psycopg2
import os

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("DB_NAME", "todo_db"),
        user=os.environ.get("DB_USER", "todo_user"),
        password=os.environ.get("DB_PASSWORD", "todo_pass")
    )

def init_db():
    for _ in range(10):  # retry 10 times
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS todos (
                    id SERIAL PRIMARY KEY,
                    title TEXT NOT NULL
                )
            """)
            conn.commit()
            cur.close()
            conn.close()
            print("✅ Database initialized")
            return
        except Exception as e:
            print("⏳ Waiting for DB...", e)
            time.sleep(2)

    raise Exception("❌ Database not ready")
