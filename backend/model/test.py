from ConnectDB import ConnectionDB
from Product import Product  # Asegúrate de importar la clase Product

db_url = "mysql://root:root123@localhost:3306/e_Commerce"
db = ConnectionDB(db_url)
print("Conexión exitosa")

db.create_Product(Product("Coca Cola", 1.5, "Refresco de cola", "imagen Coca Cola", "Bebidas", 100))
db.create_Product(Product("Pepsi", 1.2, "Refresco de cola", "imagen Pepsi", "Bebidas", 400))
db.create_Product(Product("Fanta", 1.9, "Refresco de naranja", "imagen Fanta", "Bebidas", 200))
db.create_Product(Product("Coca Cola", 1.5, "Refresco de cola", "imagen Coca Cola", "Bebidas", 100))
db.create_Product(Product("Blue Label", 1.2, "Es un Elixir", "img", "trago", 1000))

db.update_price(55, 2)
db.update_discount(56, 10)
db.update_description(57, "Refreso de colaa")

print("-------------------------")
print("Lista de productos")
listaProductos = db.show_Products()
for producto in listaProductos:
    print(producto)
print("-------------------------")
