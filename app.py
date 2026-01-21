from flask import Flask
from src.routes.todo import todo_bp
from src.routes.frontend import frontend_bp
from src.db import init_db

app = Flask(__name__)
app.register_blueprint(todo_bp)
app.register_blueprint(frontend_bp)

if __name__ == "__main__":
    init_db()  # SAFE DB INIT
    app.run(host="0.0.0.0", port=5000)
