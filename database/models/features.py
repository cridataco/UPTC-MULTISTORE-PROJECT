from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .sql_base import Base

class Features(Base):
    __tablename__ = "features"

    id_feature = Column(Integer, primary_key=True, autoincrement=True) # pk id
    feature_name = Column(String(30), nullable=True)
    
    product_features = relationship("ProductFeatures")