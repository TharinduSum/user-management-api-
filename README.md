# User Management API (FastAPI + MySQL)

A simple, clean, and production-ready **User Management REST API** built using **FastAPI** and **MySQL 8.0**.
This project is designed for **learning backend fundamentals** and is suitable for **associate software / data engineering interviews**.

---

## 🚀 Tech Stack

* **FastAPI** – High-performance Python web framework
* **MySQL 8.0 (Docker)** – Relational database
* **SQLAlchemy** – ORM for database operations
* **Pydantic** – Data validation
* **Uvicorn** – ASGI server
* **Docker** – MySQL container

---

## 📁 Project Structure

```text
user-management-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── init_db.py
│   └── routers/
│       └── users.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Prerequisites

Make sure you have the following installed:

* Python **3.10+**
* Docker
* Git

---

## 🐳 MySQL Setup (Docker)

Pull MySQL image:

```bash
docker pull mysql:8.0.44
```

Run MySQL container:

```bash
docker run -d \
  --name mysql-fastapi \
  -e MYSQL_ROOT_PASSWORD=root123 \
  -e MYSQL_DATABASE=user_management \
  -e MYSQL_USER=fastapi_user \
  -e MYSQL_PASSWORD=fastapi123 \
  -p 3306:3306 \
  mysql:8.0.44
```

Verify container:

```bash
docker ps
```

---

## 🧪 Environment Variables

Create a `.env` file in the project root:

```env
DB_USER=fastapi_user
DB_PASSWORD=fastapi123
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=user_management
```

> ⚠️ Do not commit `.env` to GitHub

---

## 🐍 Virtual Environment Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

From the **project root directory**:

```bash
uvicorn app.main:app --reload
```

API will be available at:

* [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📌 API Endpoints

| Method | Endpoint    | Description    |
| ------ | ----------- | -------------- |
| POST   | /users      | Create a user  |
| GET    | /users      | Get all users  |
| GET    | /users/{id} | Get user by ID |

---

## 🧠 What This Project Demonstrates

* Clean FastAPI project structure
* Dependency Injection
* Database integration with MySQL
* Docker-based database setup
* Pydantic validation
* RESTful API design

---

## 🛠️ Future Improvements

* Update & delete users
* Email uniqueness validation
* JWT authentication
* Pagination & filtering
* Dockerize FastAPI app
* Alembic migrations

---

## 👨‍💻 Author

**Tharindu Sumanarathna**
Computer Engineering Undergraduate
University of Jaffna

---

## 📄 License

This project is for **educational purposes**.
