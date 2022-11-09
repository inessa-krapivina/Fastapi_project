from sqlmodel import create_engine, SQLModel, Session


engine = create_engine(
    "postgresql://admin:123123@db:5432/db"
)


def create_tables():
    SQLModel.metadata.create_all(engine)
