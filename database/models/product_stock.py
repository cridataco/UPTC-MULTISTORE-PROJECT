from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from .sql_base import Base


class ProductStock(Base):
    __tablename__ = "product_stock"

    SKU = Column(String(30), primary_key=True)  # pk id
    id_product = Column(Integer, ForeignKey("product.id_product"), nullable=False)  # fk product
    date_update = Column(Date, nullable=False)
    date_of_expiry = Column(Date, nullable=True)
    current_stock = Column(Integer, nullable=False)

    # Many product stock can be from One product
    product = relationship("Product", back_populates="product_stock")
    order_details = relationship("OrderDetails")
