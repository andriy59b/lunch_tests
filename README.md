# Lunch Voter API

This Django project provides a backend service that allows employees to vote for restaurant menus before lunch. Built with Django + DRF, uses JWT for authentication, PostgreSQL as the database, and Docker for containerization.

## Tech Stack

- Python 3.11
- Django
- Django REST Framework
- PostgreSQL
- Docker + docker-compose
- JWT (djangorestframework-simplejwt)
- Pytest
- flake8

## Installing using GitHub

1. Clone the repository

```bash
git clone https://github.com/andriy59b/lunch_tests.git
cd lunch-test
cd lunch-voter
```

2. Set up virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

3. Configure Environment Variables:

- Create a .env file in the project root.
- Make sure it includes all the variables listed in the .env.sample file.
- Ensure that the variable names and values match those in the sample file.

```bash
set POSTGRES_HOST=<your db hostname>
set POSTGRES_DB=<your db name>
set POSTGRES_USER=<your db username>
set POSTGRES_PASSWORD=<your db user password>
set SECRET_KEY=<your secret key>
set DEBUG=<DEBUG> #True or False
python manage.py migrate
```

4. Run the Server:

```bash
python manage.py runserver
```

## Run with Docker

Docker should be installed

```bash
docker-compose up --build
```

The project will be available at: http://localhost:8000

## Initial Setup

In a new terminal window:

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

## JWT Authentication

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

## API Endpoints

| Method | Endpoint               | Description                |
| ------ | ---------------------- | -------------------------- |
| POST   | `/api/token/`          | Obtain JWT token           |
| POST   | `/api/token/refresh/`  | Refresh JWT token          |
| GET    | `/api/menus/`          | List all menus             |
| GET    | `/api/menus/?today=1`  | Get today's menu           |
| POST   | `/api/vote/<menu_id>/` | Vote for a specific menu   |
| GET    | `/api/results/`        | Get today's voting results |

## Run Tests

```bash
docker-compose exec web pytest
```

## Code Style Check

```bash
flake8 .
```
