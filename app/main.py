from fastapi import FastAPI
from app.routers import users

app = FastAPI(title="User Management API with MySQL")

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "API is running"}
