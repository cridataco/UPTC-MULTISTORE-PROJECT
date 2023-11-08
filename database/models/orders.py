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
    estimated_delivery_date = Column(Date, nullable=False)
    shipping_cost = Column(Numeric(precision=8, scale=2), nullable=True)
    order_note = Column(String(500), nullable=True)
    completed_delivery_date = Column(Date, nullable=True)

    # Many orders can belong to One user
    user = relationship("User", back_populates="orders")
    # Many orders can have One shipping address
    shipping_address = relationship("ShippingAddress", back_populates="orders")
    # Many orders can use One coupon
    coupon = relationship("Coupons", back_populates="orders")
    ratings = relationship("Ratings")
    order_details = relationship("OrderDetails")

    def __init__(
        self,
        order_date,
        order_state,
        payment_method,
        estimated_delivey_date,
        shipping_cost = None,
        order_note = None,
        completed_delivey_date = None
    ):
        self.order_date = order_date
        self.order_state = order_state
        self.payment_method = payment_method
        self.estimated_delivery_date =  estimated_delivey_date
        self.shipping_cost = shipping_cost
        self.order_note = order_note
        self.completed_delivery_date = completed_delivey_date
