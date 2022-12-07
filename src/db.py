from datetime import datetime

from sqlmodel import Field, Session, SQLModel, create_engine


class UserResponse(SQLModel):
    name: str
    date: datetime


class User(UserResponse, table=True):
    id: int = Field(default=None, primary_key=True)


engine = create_engine("postgresql://admin:123123@db:5432/db")


def create_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
