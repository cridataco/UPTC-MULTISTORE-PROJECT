from Product import Product
print("holi.")

db_url = "mysql://root:root123@localhost:3306/e_Commerce"

Product.add_product(1, "Product 2", 100, "Description 1", "Image 1", "Category 1", db_url)
Product.add_product(20, "Product 3", 200, "Description 2", "Image 2", "Category 2", db_url)
Product.add_product(3, "Product 4", 300, "Description 3", "Image 3", "Category 3", db_url)
Product.add_product(4, "Product 5", 400, "Description 4", "Image 4", "Category 4", db_url)

Product.delete_product(4, db_url)

Product.update_Description(20, "Description 2.1", db_url)

Product.update_Stock(3, 400, db_url)

Product.apply_discount(20, 10, db_url)

Product.update_price(1, 999, db_url)

Product.update_category(1, "Best Product", db_url)



