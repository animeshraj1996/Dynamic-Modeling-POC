import sys, asyncio
sys.path.append('../')
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from models import *
from config.database import engine, SessionLocal
from common.utilities import get_model_name
import os
import subprocess
import signal

app = FastAPI()

# Added since running pytest is not supported in FastAPI using Python 3.8
if sys.platform == "win32" and (3, 8, 0) <= sys.version_info < (3, 9, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get('/api/info')
async def read_all_info(region_name: str, db: Session = Depends(get_db)):
    modelName = get_model_name(region_name)
    return db.query(modelName).all()



