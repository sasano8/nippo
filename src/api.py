from fastapi import FastAPI, Depends
from .db import session, Session
from .models import Diary

app = FastAPI()

@app.post("/list/diary")
def list_diary(db: Session = Depends(session)):
  stmt = Diary.select()
  results = db.exec(stmt)
  return results.scalars().all()


  
@app.post("/create/diary")
def create_diary(db: Session = Depends(session), *, diary: Diary):
  diary.id = None
  db.add(diary)
  db.flush()
  return diary


  
# import uvicorn

# if __name__ == "__main__":
#   uvicorn.run("src.api:app", host="0.0.0.0", port=8000, reload=True)
