# Smart Task Management System

A full-stack Task Management System built using Python, Flask, PostgreSQL, REST APIs, Pandas, NumPy, and WebSockets featuring authentication, real-time updates, analytics dashboard, and responsive UI.

---

## Features

* 🔐 User Registration, Login & Logout
* ✅ REST API for Task Management (CRUD Operations)
* 🐘 PostgreSQL Database Integration
* 📊 Analytics Dashboard using Pandas & NumPy
* 🔔 Real-time Task Updates using WebSockets
* 🎨 Responsive Frontend using HTML & CSS

---

## Tech Stack

* Python 3.11
* Flask
* Flask-SQLAlchemy
* Flask-Login
* Flask-SocketIO
* PostgreSQL
* Pandas
* NumPy
* HTML
* CSS
* JavaScript

---

## Project Structure

```bash
smart-task-management-system/
│
├── app/
│   ├── routes/
│   │   ├── auth.py
│   │   ├── tasks.py
│   │   ├── analytics.py
│   │   └── main.py
│   │
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   │
│   ├── templates/
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   └── base.html
│   │
│   ├── models.py
│   ├── sockets.py
│   └── __init__.py
│
├── config.py
├── requirements.txt
├── run.py
├── schema.sql
├── README.md
└── .env.example
```

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/SUPRIYAMARRI/smart-task-management-system.git
cd smart-task-management-system
```

---

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

---

### 3. Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
source .venv/bin/activate
```

---

### 4. Install Required Packages

```bash
pip install -r requirements.txt
```

---

### 5. Configure Environment Variables

Create a `.env` file in the root directory and add:

```env
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/smart_tasks
```

---

### 6. Setup PostgreSQL Database

Make sure PostgreSQL is installed and running.

Run the schema file:

```bash
psql -U postgres -f schema.sql
```

---

### 7. Run the Application

```bash
python run.py
```

---

### 8. Open in Browser

```bash
http://localhost:5000
```

---

## Application Features

### Authentication

* User Registration
* User Login
* Logout Functionality
* Password Hashing

---

### Task Management APIs

| Method | Endpoint          | Description    |
| ------ | ----------------- | -------------- |
| GET    | `/api/tasks`      | Get all tasks  |
| POST   | `/api/tasks`      | Add new task   |
| PUT    | `/api/tasks/<id>` | Update task    |
| PATCH  | `/api/tasks/<id>` | Partial update |
| DELETE | `/api/tasks/<id>` | Delete task    |

---

## Task Fields

Each task contains:

* Title
* Description
* Priority
* Status
* Created Date

---

## Analytics Module

Using Pandas & NumPy:

* Total Tasks
* Completed Tasks
* Pending Tasks
* Completion Percentage
* Tasks by Priority

---

## WebSocket Features

Implemented using Flask-SocketIO:

* Real-time task updates
* Live notifications
* Instant dashboard refresh

---

## Database Schema

Database schema is available in:

```bash
schema.sql
```

---

## Submission Requirements Completed

✅ GitHub Repository
✅ PostgreSQL Schema
✅ REST APIs
✅ Flask Authentication
✅ Pandas & NumPy Analytics
✅ WebSocket Integration
✅ Responsive Frontend
✅ README Documentation

---

## Author

Supriya Marri

---

## License

MIT License
