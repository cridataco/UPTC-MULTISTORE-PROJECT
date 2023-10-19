from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProductStock(Base):
    __tablename__ = "product_stock"

    SKU = Column(String(30), primary_key=True, autoincrement=True)  # pk id
    id_product = Column(Integer, ForeignKey("product.id_product"), nullable=False)  # fk product
    date_update = Column(Date, nullable=False)
    date_of_expiry = Column(Date, nullable=True)
    current_stock = Column(Integer, nullable=False)
    
    order_details = relationship("ProductDetails")

