from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from .sql_base import Base

class Orders(Base):
    __tablename__ = "orders"

    id_order = Column(Integer, primary_key=True, autoincrement=True)  # pk id
    id_user = Column(Integer, ForeignKey("users.id_user"), nullable=False)  # fk users
    order_date = Column(Date, nullable=False)
    order_state = Column(String(15), nullable=False)
    payment_method = Column(String(7), nullable=False)
    id_coupon = Column(
        Integer, ForeignKey("coupons.id_coupon"), nullable=True
    )  # fk coupon
    id_address = Column(
        Integer, ForeignKey("shipping_address.id_address"), nullable=False
    )  # fk shipping_address
    shipping_cost = Column(Numeric(precision=8, scale=2), nullable=True)
    order_note = Column(String(500), nullable=True)
    estimated_delivery_date = Column(Date, nullable=False)
    completed_delivery_date = Column(Date, nullable=True)

    # Many orders can belong to One user
    user = relationship("User", back_populates="orders")
    # Many orders can have One shipping address
    shipping_address = relationship("ShippingAddress", back_populates="orders")
    # Many orders can use One coupon
    coupon = relationship("Coupons", back_populates="orders")
    ratings = relationship("Ratings")
    order_details = relationship("OrderDetails")
