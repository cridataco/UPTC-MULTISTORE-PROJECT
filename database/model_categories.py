from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Categories(Base):
    __tablename__ = "categories"

    id_category = Column(Integer, primary_key=True, autoincrement=True) # pk id
    id_subcategory = Column(Integer, ForeignKey("categories.id_subcategory"), nullable=True) # fk categories
    category_name = Column(String(30), nullable=False)
    description = Column(String(23), nullable=True)
    
    categories = relationship("Categories")