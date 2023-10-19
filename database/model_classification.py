from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Classification(Base):
    __tablename__ = "classification"

    id_product = Column(
        Integer, ForeignKey("product.id_product"), primary_key=True, nullable=False
    )  # fk product
    id_category = Column(
        Integer, ForeignKey("categories.id_category"), primary_key=True, nullable=False
    )  # fk categories
    
