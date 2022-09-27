import sys
sys.path.append('../')
from sqlalchemy import Column, Integer, String
from config.database import Base
from config.conf import DB_SCHEMA_NAME



class Info_MX(Base):
    __tablename__ = 'info_mx'
    __table_args__ = {'extend_existing': True} 

    
    id = Column(Integer, primary_key=True)
    channel = Column(String)