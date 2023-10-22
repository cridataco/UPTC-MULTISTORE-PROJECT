from sqlalchemy import Column, String, Integer, Numeric, BINARY, ForeignKey
from sqlalchemy.orm import relationship
from .sql_base import Base


class OrderDetails(Base):
    __tablename__ = "order_details"

    SKU = Column(
        String(30), ForeignKey("product_stock.SKU"), primary_key=True, nullable=False
    )  # fk product_stock
    id_order = Column(
        Integer, ForeignKey("orders.id_order"), primary_key=True, nullable=False
    )  # fk orders
    quantity = Column(BINARY, nullable=False)
    sale_price = Column(Numeric(precision=10, scale=2), nullable=False)

    # Many order details can be from One order
    order = relationship("Orders", back_populates="order_details")
    # Many order details can have One product stock
    product_stock = relationship("ProductStock", back_populates="order_details")
