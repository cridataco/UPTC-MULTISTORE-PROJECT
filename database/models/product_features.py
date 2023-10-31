from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .sql_base import Base


class ProductFeatures(Base):
    __tablename__ = "product_features"

    id_product = Column(
        Integer, ForeignKey("product.id_product"), primary_key=True, nullable=False
    )  # fk product
    id_feature = Column(
        Integer, ForeignKey("features.id_feature"), primary_key=True, nullable=False
    )  # fk features
    feature_value = Column(String(30), nullable=True)

    # Many product features can be from One product
    product = relationship("Product", back_populates="product_features")
    # Many product features can be One feature
    feature = relationship("Features", back_populates="product_features")


    def __init__(self, feature_value=None):
        self.feature_value = feature_value
