import sys
sys.path.append('../')
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from models import *
from config.database import engine, SessionLocal, DB_SCHEMA_NAME
from common.utilities import get_model_name

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get('/api/info')
async def read_all_info(db: Session = Depends(get_db)):
    modelName = get_model_name()
    return db.query(modelName).all()