# 🍽️ Lunch Voter API

A backend service that allows employees to vote for restaurant menus before lunch. Built with Django + DRF, uses JWT for authentication, PostgreSQL as the database, and Docker for containerization.

---

## 🔧 Tech Stack

- Python 3.11
- Django
- Django REST Framework
- PostgreSQL
- Docker + docker-compose
- JWT (djangorestframework-simplejwt)
- Pytest
- flake8

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/lunch-voter.git
cd lunch-voter
```

### 2. Build and run with Docker

```bash
docker-compose up --build
```

🌐 The project will be available at:  
[http://localhost:8000](http://localhost:8000)

---

## ⚙️ Initial Setup

In a new terminal window:

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

---

## 📦 Run locally without Docker (optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🔑 JWT Authentication

### Get token:

```
POST /api/token/
```

Request body:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

### Refresh token:

```
POST /api/token/refresh/
```

---

## 📡 API Endpoints

| Method | Endpoint               | Description                |
| ------ | ---------------------- | -------------------------- |
| POST   | `/api/token/`          | Obtain JWT token           |
| POST   | `/api/token/refresh/`  | Refresh JWT token          |
| GET    | `/api/menus/`          | List all menus             |
| GET    | `/api/menus/?today=1`  | Get today's menu           |
| POST   | `/api/vote/<menu_id>/` | Vote for a specific menu   |
| GET    | `/api/results/`        | Get today's voting results |

---

## 🧪 Run Tests

```bash
docker-compose exec web pytest
```

---

## 🎯 Code Style Check

```bash
flake8 .
```

---

## 📄 License

MIT License

---

## 🗄️ Connecting to the PostgreSQL Database

If you want to connect directly to the PostgreSQL database (e.g. using DBeaver, pgAdmin or psql), use the following credentials:

- **Host:** localhost
- **Port:** 5432
- **Database name:** lunch_db
- **Username:** postgres
- **Password:** 199887766

> Note: If you are using Docker, make sure the `db` container is running.
