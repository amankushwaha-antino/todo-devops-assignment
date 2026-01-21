# Todo App

Simple Flask + PostgreSQL Todo app with a Vue frontend.

## Features
- Create, read, update, delete tasks via REST API


## Quick start (Docker)
1. Build and start services:

```bash
# Todo App

Simple Flask + PostgreSQL Todo app with a Vue frontend.

## Features
- Create, read, update, delete tasks via REST API


## Quick start (Docker) — recommended
1. Build and start services (this starts the Flask app and Postgres DB):

```bash
docker compose up --build
```

2. Open the UI in your browser: http://localhost:5000/

## Quick start (local / venv) — advanced
Running the app directly via `app.py` is possible but requires a running PostgreSQL instance and correct environment variables. This is intended for advanced development only.

1. Ensure PostgreSQL is running and reachable, and set the DB environment variables (example):

```powershell
$env:DB_HOST = 'localhost'
$env:DB_NAME = 'todo_db'
$env:DB_USER = 'todo_user'
$env:DB_PASSWORD = 'todo_pass'
```

2. Create and activate a venv (Windows):

```powershell
python -m venv venv
venv\Scripts\Activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python app.py
```

Note: If you run locally (not via Docker) you are responsible for providing the database; the app's `init_db()` will attempt to create the `todos` table but cannot start a DB for you.

## API Endpoints
- GET `/api/todos/` — list all tasks (returns JSON array of `{ id, title }`)
- POST `/api/todos/` — create task (body `{ title: string }`)
- PUT `/api/todos/<id>` — update task (body `{ title: string }`)
- DELETE `/api/todos/<id>` — delete task

## UI Notes
- The homepage (`/`) uses Vue and Bootstrap.
- Use the **Get All Tasks** button to fetch every task from the server.
- Use **Show Recent** to view the latest 5 tasks.

## Database
- The app expects a PostgreSQL database. When started, `app.py` calls `init_db()` which will create the `todos` table if missing.
- When running with Docker Compose the DB service and credentials are configured in `docker-compose.yml`.

## Development tips
- To inspect the DB (docker):

```bash
docker exec -it <db_container> psql -U todo_user -d todo_db
```

- If you change templates or frontend code, refresh the browser; with Docker you may need to rebuild.

## Files of interest
- `app.py` — app entrypoint
- `src/routes/todo.py` — API routes
- `templates/index.html` — frontend UI
- `src/db.py` — DB connection & init

---
If you want, I can run the app now and verify the UI in a browser or add a small modal to show tasks.