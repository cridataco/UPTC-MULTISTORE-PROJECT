from sqlalchemy import Column, Integer, Numeric, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PriceHistory(Base):
    __tablename__ = "price_history"

    id_history = Column(Integer, primary_key=True, autoincrement=True) # pk id
    id_product = Column(Integer, ForeignKey("product.id_product"), nullable=False) # fk product
    start_date = Column(Date, nullable=False)
    finish_date = Column(Date, nullable=False)
    purchase_price = Column(Numeric(precision=10, scale=2), nullable=True)
    