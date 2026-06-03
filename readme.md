# Task Manager API

A RESTful API for managing tasks, built with FastAPI and PostgreSQL.

---

## Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL
- **Server:** Gunicorn + Uvicorn
- **Process Manager:** systemd

---

## Prerequisites

- Python 3.10+
- PostgreSQL
- pip

---

## Installation
```bash
git clone <repo-url>
cd project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Create a `.env` file:

env
DATABASE_URL=postgresql://user:password@localhost:5432/taskdb

Run database migrations:

bash
alembic upgrade head

---

## Running Locally

bash
uvicorn app.main:app --reload

API docs available at: `http://localhost:8000/docs`

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | List all tasks |
| POST | `/tasks` | Create a task |
| GET | `/tasks/{id}` | Get a task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

---

## Deployment (Linux)

**1. Install Gunicorn:**

bash
pip install gunicorn uvicorn

**2. Create systemd service:**

ini
# /etc/systemd/system/taskmanager.service

[Unit]
Description=Task Manager API
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/project
ExecStart=/home/ubuntu/project/venv/bin/gunicorn \
-w 4 -k uvicorn.workers.UvicornWorker \
app.main:app --bind 0.0.0.0:8000
Restart=always

[Install]
WantedBy=multi-user.target

**3. Enable and start:**

bash
sudo systemctl daemon-reload
sudo systemctl enable taskmanager
sudo systemctl start taskmanager
sudo systemctl status taskmanager
