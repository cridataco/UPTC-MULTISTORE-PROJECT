from sqlalchemy import Column, Integer, String, Numeric, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Coupons(Base):
    __tablename__ = "coupons"

    id_coupon = Column(Integer, primary_key=True, autoincrement=True)  # pk id
    coupon_code = Column(String(10), nullable=False)
    discount = Column(Numeric(precision=12, scale=2),  nullable=False)
    due_date = Column(Date, nullable=False)
    restrictions = Column(String(100), nullable=False)
    
    orders = relationship("Orders")
    