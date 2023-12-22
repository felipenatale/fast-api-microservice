from sqlalchemy import Column, Integer, String, Numeric, DateTime
from database.db_config import Base
from pydantic import BaseModel

class Client(Base):
    __tablename__ = 'client'

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    id = Column(Integer, primary_key=True)
    name = Column(String)
    document = Column(String)
    address = Column(String)
    created_at = Column(DateTime)
    deleted_at = Column(DateTime)
    
    def __repr__(self):
        return f'id: {self.id}, name: {self.name}'

class ClientSchema(BaseModel):
    name : str
    document : str
    address : str
    created_at: str

class UpdateSchema(BaseModel):
    address : str