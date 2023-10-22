from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .sql_base import Base


class Resources(Base):
    __tablename__ = "resources"

    id_resource = Column(String(20), primary_key=True)  # pk id
    id_product = Column(Integer, ForeignKey("product.id_product"), nullable=False)  # fk product
    feature_name = Column(String(20), nullable=False)
    weight_resource = Column(String(10), nullable=False)
    format = Column(String(5), nullable=False)
    resource_type = Column(String(10), nullable=False)
    resource_url = Column(String(100), nullable=False)

    # Many resources can be from One product
    product = relationship("Product", back_populates="resources")
