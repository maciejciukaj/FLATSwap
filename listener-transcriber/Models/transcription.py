from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from Models.stations import Stations

Base = declarative_base()

class Transcriptions(Base):
    __tablename__ = 'Transcriptions'
    Id = Column(Integer, primary_key=True)
    StationId = Column('StationId',Integer, ForeignKey(Stations.Id), nullable=False)
    TranscribedText = Column(String, nullable=False)
    Frequency = Column(String, nullable=False)
    Timestamp = Column(DateTime, nullable=False)