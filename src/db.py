from sqlmodel import SQLModel, create_engine, Session

from .models import Diary


sqlite_file_name = "dialy.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)


def session():
    with Session(engine) as db:
        yield db
        db.commit()
