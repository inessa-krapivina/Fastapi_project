from fastapi import FastAPI
import uvicorn
from src.db import create_tables, engine, User, get_session
import platform
from datetime import datetime


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_tables()


def create_user():
    with get_session() as session:
        user = User(
            name=platform.node(),
            date=str(datetime.now())
        )
        session.add(user)
        session.commit()

        session.refresh(user)
        return user


@app.get("/")
def read_users() -> User:
    with get_session() as session:
        statement = select(User).where(User.name == platform.node())
        results = session.exec(statement)

        users = results.all()
        if not users:
            user = create_user()
            return user

        create_user()
        user = users[-1]
        return user
