from sqlalchemy import Column, String, Integer, Numeric, BINARY, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


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
