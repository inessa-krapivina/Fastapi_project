from sqlmodel import create_engine, SQLModel, Session, Field
from typing import Optional
from datetime import datetime


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: Optional[str]
    date: datetime


engine = create_engine(
    "postgresql://admin:123123@db:5432/db"
)


def create_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
