from fastapi import FastAPI, Depends
from sqlmodel import select, Session
from src.db import create_tables, User, UserResponse, get_session
import platform
from datetime import datetime


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_tables()


def create_user(session):
    user = User(
        name=platform.node(),
        date=datetime.now()
    )
    session.add(user)
    session.commit()

    session.refresh(user)
    return user


@app.get("/", response_model=UserResponse)
def read_users(session: Session = Depends(get_session)) -> UserResponse:
    statement = select(User).where(User.name == platform.node())
    results = session.exec(statement)

    users = results.all()
    if not users:
        user = create_user(session)
        return user

    user = User(**users[-1].dict())
    create_user(session)
    return user
