from typing import List
from uuid import uuid4
from fastapi import FastAPI

from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Jafar",
        last_name="Sadik",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Nusrat",
        last_name="Jahan Shoshi",
        gender=Gender.female,
        roles=[Role.student]
    )
]

@app.get("/")
async def root():
    #await foo()
    return {"Hello": "Mars"}

@app.get("/api/v1/users")
async def fetch_users():
    return db