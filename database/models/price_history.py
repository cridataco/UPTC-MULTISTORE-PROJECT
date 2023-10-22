from sqlalchemy import Column, Integer, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from .sql_base import Base


class PriceHistory(Base):
    __tablename__ = "price_history"

    id_history = Column(Integer, primary_key=True, autoincrement=True)  # pk id
    id_product = Column(Integer, ForeignKey("product.id_product"), nullable=False)  # fk product
    start_date = Column(Date, nullable=False)
    finish_date = Column(Date, nullable=False)
    purchase_price = Column(Numeric(precision=10, scale=2), nullable=True)

    # Many price history can be from One product
    product = relationship("Product", back_populates="price_history")
