from sqlmodel import Field, SQLModel

from typing import Optional
from datetime import datetime,timezone, timedelta
from sqlalchemy import select


LOCAL_TIMEZONE = datetime.now(timezone(timedelta(0))).astimezone().tzinfo

def utc_now():
    now = datetime.now(LOCAL_TIMEZONE)
    return now

class Crud(SQLModel):
    @classmethod
    def select(cls, *columns):
        if columns:
            return select(*columns)
        else:
            return select(cls)


class Diary(Crud, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    start_at: datetime = Field(default_factory=utc_now)
    end_at: datetime = Field(default_factory=utc_now)
    working_at: datetime = Field(default_factory=utc_now)
    text1: str
    text2: str
    locked: bool = False
    

        