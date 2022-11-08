from fastapi import FastAPI
import uvicorn
from database.db import create_tables, get_session, engine
from database.models import User
from sqlmodel import Session, select
from typing import Optional
import platform
from datetime import datetime


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_tables()


def create_user():
    with Session(engine) as session:
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
    with Session(engine) as session:
        statement = select(User).where(User.name == platform.node())
        results = session.exec(statement)

        users = results.all()
        if not users:
            user = create_user()
            return user

        create_user()
        user = users[-1]
        return user



if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
