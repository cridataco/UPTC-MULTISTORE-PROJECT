from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ShippingAddress(Base):
    __tablename__ = "shipping_address"

    id_address = Column(Integer, primary_key=True, autoincrement=True)  # pk id
    id_user = Column(Integer, ForeignKey("users.id_user"), nullable=False)  # fk users
    id_place = Column(Integer, ForeignKey("places.id_place"), nullable=True)  # fk places
    shipping_address = Column(String(100), nullable=False)
    shipment_receiver_name = Column(String(30), nullable=False)
    receiver_phone = Column(String(10), nullable=True)
    address_details = Column(String(50), nullable=True)
    
    orders = relationship("Orders")
    
