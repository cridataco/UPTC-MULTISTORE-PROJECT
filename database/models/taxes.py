from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import relationship
from .sql_base import Base

class Taxes(Base):
    __tablename__ = "taxes"

    id_tax = Column(Integer, primary_key=True, autoincrement=True)  # pk id
    tax_value = Column(Float(3), nullable=False)

    products = relationship("Product", back_populates="tax")

    #Constructor
    def __init__(self, tax_value):
        self.tax_value = tax_value
        
    def create_tax(cls, session, tax_value: float):
        new_tax = cls(tax_value=tax_value)
        session.add(new_tax)
        session.commit()
        return new_tax
    
    def read_tax(cls, session, tax_id: int):
        tax = session.query(cls).get(tax_id)
        return tax