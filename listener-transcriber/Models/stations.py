from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Stations(Base):
    __tablename__ = 'Stations'
    Id = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)
    Country = Column(String, nullable=False)
    Description = Column(String, nullable=False)
