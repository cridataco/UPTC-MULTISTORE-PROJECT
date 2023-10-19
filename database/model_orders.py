from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Orders(Base):
    __tablename__ = "orders"

    id_order = Column(Integer, primary_key=True, autoincrement=True)  # pk id
    id_user = Column(Integer, ForeignKey("users.id_user"), nullable=False)  # fk users
    order_date = Column(Date, nullable=False)
    order_state = Column(String(15), nullable=False)
    payment_method = Column(String(7), nullable=False)
    id_coupon = Column(Integer, ForeignKey("coupons.id_coupon"), nullable=True)
    id_address = Column(Integer, ForeignKey("shipping_address.id_address"), nullable=False)
    shipping_cost = Column(Numeric(precision=8, scale=2), nullable=True)
    order_note = Column(String(500), nullable=True)
    estimated_delivery_date = Column(Date, nullable=False)
    completed_delivery_date = Column(Date, nullable=True)  

    ratings = relationship("Ratings")
    order_details = relationship("OrderDetails")
