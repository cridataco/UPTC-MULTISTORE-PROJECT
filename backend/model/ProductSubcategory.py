from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ProductSubcategory(Base):
    __tablename__ = "product_subcategories"

    id_subcategory = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey("product_categories.id_category"))
    name_subcategory = Column(String(100), nullable=False)
    description_subcategory = Column(String(250), nullable=True)

    category = relationship("ProductCategory", back_populates="subcategories")

    def __init__(self, category, name_subcategory, description_subcategory):
        self.category = category
        self.name_subcategory = name_subcategory
        self.description_subcategory = description_subcategory

    def __str__(self):
        return (
            f"Subcategory: {self.name_subcategory}\n"
            f"Category: {self.category.name_category}\n"
            f"Description: {self.description_subcategory}\n"
        )
