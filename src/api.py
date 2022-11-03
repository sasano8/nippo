from fastapi import FastAPI, Depends
from .db import session, Session
from .models import Diary

app = FastAPI()

@app.post("/list/diary")
def list_diary(db: Session = Depends(session)):
  stmt = Diary.select()
  results = db.exec(stmt)
  return list(dict(**x) for x in results)
"""
# Diaryが邪魔
{
    "Diary": {
      "working_at": "2022-11-03T01:27:24.922000",
      "id": 0,
      "text2": "string",
      "start_at": "2022-11-03T01:27:24.922000",
      "end_at": "2022-11-03T01:27:24.922000",
      "text1": "string",
      "locked": false
    }
  }
"""

  
@app.post("/create/diary")
def create_diary(db: Session = Depends(session), *, diary: Diary):
  db.add(diary)
  return diary


  
# import uvicorn

# if __name__ == "__main__":
#   uvicorn.run("src.api:app", host="0.0.0.0", port=8000, reload=True)
