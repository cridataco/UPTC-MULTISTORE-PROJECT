from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .sql_base import Base


class Categories(Base):
    __tablename__ = "categories"

    id_category = Column(Integer, primary_key=True, autoincrement=True)  # pk id
    id_subcategory = Column(
        Integer, ForeignKey("categories.id_category"), nullable=True
    )  # fk categories
    category_name = Column(String(30), nullable=False)
    description = Column(String(23), nullable=True)

    # One category can have Many sub-categories
    sub_categories = relationship(
        "Categories", remote_side=[id_category]
    )
    # One category can have Many classifications
    classifications = relationship("Classification", back_populates="category")


    def __init__(self, category_name, description=None):
        self.category_name = category_name
        self.description = description
