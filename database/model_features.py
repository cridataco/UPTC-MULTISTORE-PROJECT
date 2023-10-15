from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Features(Base):
    __tablename__ = "features"

    id_feature = Column(Integer, primary_key=True, autoincrement=True) # pk id
    feature_name = Column(String(30), nullable=True)
    
    product_features = relationship("ProductFeatures")