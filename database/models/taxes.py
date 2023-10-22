from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import relationship
from .sql_base import Base

class Taxes(Base):
    __tablename__ = "taxes"

    id_tax = Column(Integer, primary_key=True, autoincrement=True)  # pk id
    tax_value = Column(Float(3), nullable=False)

    products = relationship("Product", back_populates="tax")
