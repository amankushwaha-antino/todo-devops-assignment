from flask import Blueprint, request, jsonify
from src.db import get_db_connection

todo_bp = Blueprint("todo", __name__, url_prefix="/api/todos")

@todo_bp.route("/", methods=["GET"])
def get_todos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title FROM todos")
    todos = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(todos)

@todo_bp.route("/", methods=["POST"])
def add_todo():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO todos (title) VALUES (%s)", (data["title"],))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Todo added"}

@todo_bp.route("/<int:id>", methods=["DELETE"])
def delete_todo(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM todos WHERE id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Todo deleted"}

@todo_bp.route("/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    data = request.json
    print("UPDATE REQUEST:", todo_id, data)

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE todos SET title=%s WHERE id=%s",
        (data["title"], todo_id)
    )

    print("ROWS AFFECTED:", cur.rowcount)

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Todo updated", "rows": cur.rowcount}

