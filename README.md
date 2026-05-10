# Smart Task Management System

Smart Task Management System is a full-stack web application developed using Python, Flask, and PostgreSQL to help users manage daily tasks efficiently. The project includes authentication, task management APIs, analytics dashboard, and real-time task updates using WebSockets.

I built this project to improve my backend development skills and learn how REST APIs, PostgreSQL, and real-time communication work in Flask applications.

---

# Features

- User Registration and Login
- Secure Authentication System
- Task Management (CRUD Operations)
- PostgreSQL Database Integration
- REST APIs for Task Handling
- Analytics Dashboard using Pandas and NumPy
- Real-time Updates using Flask-SocketIO
- Responsive Frontend using HTML, CSS, and JavaScript

---

# Tech Stack

- Python 3.11
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-SocketIO
- PostgreSQL
- Pandas
- NumPy
- HTML
- CSS
- JavaScript

---

# Project Structure

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

# Installation and Setup

## 1. Clone the Repository

```bash
git clone https://github.com/SUPRIYAMARRI/smart-task-management-system.git

cd smart-task-management-system
```

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

## 3. Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

## 4. Install Required Packages

```bash
pip install -r requirements.txt
```

## 5. Configure Environment Variables

Create a `.env` file in the root directory and add the following:

```env
SECRET_KEY=your_secret_key

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/smart_task
```

---

# PostgreSQL Database Setup

Make sure PostgreSQL is installed and running on your system.

Run the schema file using:

```bash
psql -U postgres -f schema.sql
```

---

# Run the Application

```bash
python run.py
```

---

# Open in Browser

```bash
http://localhost:5000
```

---

# Authentication Features

- User Registration
- User Login
- Logout Functionality
- Password Hashing for Security

---

# Task Management REST APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks` | Get all tasks |
| POST | `/api/tasks` | Create new task |
| PUT | `/api/tasks/<id>` | Update full task |
| PATCH | `/api/tasks/<id>` | Partial update |
| DELETE | `/api/tasks/<id>` | Delete task |

---

# Task Fields

Each task contains:

- Title
- Description
- Priority
- Status
- Created Date

---

# Analytics Dashboard

The analytics module is developed using Pandas and NumPy.

It provides:

- Total Tasks
- Completed Tasks
- Pending Tasks
- Completion Percentage
- Tasks Based on Priority

---

# WebSocket Features

Implemented using Flask-SocketIO:

- Real-time Task Updates
- Live Notifications
- Instant Dashboard Refresh

---

# Database Schema

Database schema is available in:

```bash
schema.sql
```

---

# Demo Video

Demo video link:

```bash
https://drive.google.com/file/d/13giau_Xve_nSndVe0vuCUyjZlbw8AmVw/view?usp=drive_link
```

---

# Project Highlights

- Full-stack Flask Application
- REST API Development
- PostgreSQL Integration
- Authentication System
- Real-time Communication using WebSockets
- Analytics using Pandas and NumPy
- Responsive User Interface

---

# Future Improvements

- Email Notifications
- Task Reminder System
- File Upload Support
- Dark Mode UI
- Admin Dashboard

---

# License

This project is licensed under the MIT License.
