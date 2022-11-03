from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.pool import StaticPool
from sqlalchemy.pool import StaticPool

sqlite_url = f"sqlite:///:inmemory:"



if "inmemory":
    # TODO: スレッドセーフじゃないので、マルチリクエストを受けるとバグる
    # TODO: in memory dbをスレッドで使用する方法（ロックしながら使う方法）
    # TODO: vercelでDBをホストする方法
    engine = create_engine("sqlite:///:memory:", echo=True, poolclass=StaticPool, connect_args={'check_same_thread': False})
    ses = Session(engine)
    def session():
        try:
            yield ses
            ses.commit()
        except Exception as e:
            print(e)
            ses.rollback()
else:
    raise Exception()


def init_table():
    from .models import Diary
    SQLModel.metadata.create_all(engine)

