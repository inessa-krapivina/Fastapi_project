from sqlmodel import create_engine, SQLModel, Session, Field
from datetime import datetime


class UserResponse(SQLModel):
    name: str
    date: datetime


class User(UserResponse, table=True):
    id: int = Field(default=None, primary_key=True)


engine = create_engine(
    "postgresql://admin:123123@db:5432/db"
)


def create_tables():
    SQLModel.metadata.create_all(engine)


get_session = lambda: Session(engine)
