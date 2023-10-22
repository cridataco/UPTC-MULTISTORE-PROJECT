from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .sql_base import Base


class ShippingAddress(Base):
    __tablename__ = "shipping_address"

    id_address = Column(Integer, primary_key=True, autoincrement=True)  # pk id
    id_user = Column(Integer, ForeignKey("users.id_user"), nullable=False)  # fk users
    id_place = Column(
        Integer, ForeignKey("places.id_place"), nullable=True
    )  # fk places
    shipping_address = Column(String(100), nullable=False)
    shipment_receiver_name = Column(String(30), nullable=False)
    receiver_phone = Column(String(10), nullable=True)
    address_details = Column(String(50), nullable=True)

    # Many shipping addresses can be from One place ?????
    place = relationship("Places", back_populates="shipping_addresses")
    # Many shipping addresses can be from One user
    user = relationship("User", back_populates="shipping_addresses")
    orders = relationship("Orders")
