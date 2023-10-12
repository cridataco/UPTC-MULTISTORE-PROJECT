from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id_product = Column(Integer, primary_key=True, autoincrement=True)
    name_product = Column(String(100), nullable=False)
    reference_model = Column(String(100), nullable=False)
    release_date = Column(DateTime, nullable=False)
    creation_date = Column(DateTime, default=func.now())
    product_features = Column(String(100), nullable=False)
    keywords = Column(String(100), nullable=False)
    product_link = Column(String(250), nullable=False)

    product_resources = relationship("ProductResource", back_populates="product")
