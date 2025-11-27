from pydantic import BaseModel
from sqlalchemy import Column, Float, Integer, String
from .database import Base

class PricePrediction(BaseModel):
    area_m2: float
    rooms: int
    floor: str
    year_built: int
    longitude: float
    latitude: float
    locality: str

class OfferDB(Base):
    __tablename__ = "offers"
    id = Column(Integer, primary_key=True)
    area_m2 = Column(Float)
    rooms = Column(Integer)
    photos = Column(Integer)
    locality = Column(String)
    street = Column(String)
    property_type = Column(String)
    city = Column(String)
    price = Column(Float)