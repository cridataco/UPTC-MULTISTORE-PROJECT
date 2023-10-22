from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .sql_base import Base

class Places(Base):
    __tablename__ = "places"

    id_place = Column(Integer, primary_key=True, autoincrement=True)  # pk id
    id_location = Column(
        Integer, ForeignKey("places.id_place"), nullable=True, autoincrement=True
    )  # fk places
    place_name = Column(String(50), nullable=False)
    place_type = Column(String(7), nullable=False)
    postal_code = Column(Integer, nullable=False)

    # One place can have Many sub-places
    sub_places = relationship("Places", back_populates="places", remote_side=[id_place])
    # Many sub-places can have Many places
    places = relationship("Places", back_populates="sub_places")
    # One place can have Many shipping addresses ????
    shipping_addresses = relationship("ShippingAddress", back_populates="place")
    
    def __init__(self, place_name, place_type, postal_code):
        self.place_name = place_name
        self.place_type = place_type
        self.postal_code = postal_code
