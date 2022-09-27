from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sys
sys.path.append('../')
from config.conf import get_db_name

# SQLALCHEMY_DATABASE_URL = "sqlite:///./dynamicModeling.db"
SQLALCHEMY_DATABASE_URL = get_db_name()


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()










