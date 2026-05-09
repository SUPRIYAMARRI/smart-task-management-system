# Smart Task Management System

A Flask + PostgreSQL task manager with REST APIs, real-time updates via WebSockets, and analytics powered by Pandas & NumPy.

## Features

- 🔐 User registration, login & logout (Flask-Login + hashed passwords)
- ✅ Full CRUD REST API for tasks (Add / Update / Delete / Get all)
- 🐘 PostgreSQL persistence via SQLAlchemy (Users + Tasks tables)
- 📊 Analytics endpoint (Total, Completed, Pending, Completion %) using Pandas & NumPy
- 🔔 Live task updates broadcast over WebSockets (Flask-SocketIO)
- 🎨 Clean responsive HTML/CSS dashboard

## Tech Stack

Python 3.10+, Flask 3, Flask-SQLAlchemy, Flask-Login, Flask-SocketIO, PostgreSQL, Pandas, NumPy, eventlet.

## Project Structure

```
smart-tasks/
├── run.py                  # Entry point (socketio.run)
├── config.py               # Config (reads .env)
├── schema.sql              # Raw PostgreSQL schema
├── requirements.txt
├── .env.example
└── app/
    ├── __init__.py         # App factory + extensions
    ├── models.py           # User, Task models
    ├── sockets.py          # WebSocket handlers + broadcaster
    ├── routes/
    │   ├── auth.py         # /register /login /logout
    │   ├── main.py         # / and /dashboard
    │   ├── tasks.py        # /api/tasks  (GET, POST, PUT, DELETE)
    │   └── analytics.py    # /api/analytics/summary
    ├── templates/          # Jinja2 templates (base, login, register, dashboard)
    └── static/             # CSS + JS
```

## Setup

### 1. Clone & install

```bash
git clone <your-repo-url>
cd smart-tasks
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. PostgreSQL database

Make sure PostgreSQL is running, then:

```bash
psql -U postgres -f schema.sql
```

(Or run the SQL inside `schema.sql` manually. The app will also auto-create tables via SQLAlchemy on first run.)

### 3. Environment

```bash
cp .env.example .env
# Edit .env: set SECRET_KEY and DATABASE_URL
```

`DATABASE_URL` format: `postgresql://USER:PASSWORD@HOST:PORT/smart_tasks`

### 4. Run

```bash
python run.py
```

Open http://localhost:5000 — register an account, log in, and start adding tasks. Open the dashboard in two browser tabs to see live WebSocket updates.

## REST API

All `/api/*` endpoints require an authenticated session (cookie from `/login`).

| Method | Endpoint                  | Description           |
|--------|---------------------------|-----------------------|
| GET    | `/api/tasks`              | List current user's tasks |
| POST   | `/api/tasks`              | Create task `{title, description, priority, status}` |
| PATCH  | `/api/tasks/<id>`         | Update any field |
| PUT    | `/api/tasks/<id>`         | Update any field |
| DELETE | `/api/tasks/<id>`         | Delete task |
| GET    | `/api/analytics/summary`  | Pandas/NumPy analytics summary |

### Example

```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -b cookies.txt \
  -d '{"title":"Ship MVP","priority":"High","status":"Pending"}'
```

## Analytics output

```json
{
  "total": 12,
  "completed": 5,
  "pending": 4,
  "in_progress": 3,
  "completion_percentage": 41.67,
  "by_priority": {"High": 4, "Medium": 6, "Low": 2}
}
```

## WebSocket events

Client connects via Socket.IO. Server broadcasts:

- `task_created` — payload: full task
- `task_updated` — payload: full task
- `task_deleted` — payload: `{ id }`

The dashboard listens to these and refreshes the list + analytics in real time.

## License

MIT
