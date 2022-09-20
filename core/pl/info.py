import sys
sys.path.append('../')
from sqlalchemy import Column, Integer, String
from config.database import Base, DB_SCHEMA_NAME


class Info_PL(Base):
    __tablename__ = 'info_pl'
    __table_args__ = {'extend_existing': True} 


    id = Column(Integer, primary_key=True)
    banner = Column(String)