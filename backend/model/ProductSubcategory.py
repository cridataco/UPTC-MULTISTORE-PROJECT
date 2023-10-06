class ProductSubcategory:
    def __init__(self, category, name_subcategory, description_subcategory):
        self.category = category
        self.name_subcategory = name_subcategory
        self.description_subcategory = description_subcategory

    def __str__(self):
        return (f"Subcategory: {self.name_subcategory} \n"
                f"Category: {self.category.name_category} \n"
                f"Description: {self.description_subcategory} \n")
