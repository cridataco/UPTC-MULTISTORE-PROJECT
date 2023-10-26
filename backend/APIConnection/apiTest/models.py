from django.db import models
from datetime import date


class ProductResource:
    def __init__(self, id_product_resource, product_length, product_width, product_height, product_weight,
                 product_dimension):
        self.id_product_resource = id_product_resource
        self.product_length = product_length
        self.product_width = product_width
        self.product_height = product_height
        self.product_weight = product_weight
        self.product_dimension = product_dimension
        self.product_url_resources = []

    @property
    def id_product_resource(self):
        return self.id_product_resource

    @id_product_resource.setter
    def id_product_resource(self, value):
        self.id_product_resource = value

    @property
    def product_length(self):
        return self.product_length

    @product_length.setter
    def product_length(self, value):
        self.product_length = value

    @property
    def product_width(self):
        return self.product_width

    @product_width.setter
    def product_width(self, value):
        self.product_width = value

    @property
    def product_height(self):
        return self.product_height

    @product_height.setter
    def product_height(self, value):
        self.product_height = value

    @property
    def product_weight(self):
        return self.product_weight

    @product_weight.setter
    def product_weight(self, value):
        self.product_weight = value

    @property
    def product_dimension(self):
        return self.product_dimension

    @product_dimension.setter
    def product_dimension(self, value):
        self.product_dimension = value

    @property
    def product_url_resources(self):
        return self.product_url_resources

    @product_url_resources.setter
    def product_url_resources(self, value):
        self.product_url_resources = value

    def add_product_url_resource(self, value):
        if value not in self.product_url_resources:
            self.product_url_resources.append(value)
        else:
            print("Error: El URL resource ya existe en la lista.")

    def remove_product_url_resource(self, value):
        if value in self.product_url_resources:
            self.product_url_resources.remove(value)

    def __str__(self):
        return f"Product ID: {self.id_product_resource}\nProduct Length: {self.product_length}\nProduct Width: {self.product_width}\nProduct Height: {self.product_height}\nProduct Weight: {self.product_weight}\nProduct Dimensions: {self.product_dimension}\nProduct URL Resources: {self.product_url_resources}"


class PriceHistory:
    def __init__(self, id_price_history, start_date, end_date, price_actual):
        self.id_price_history = id_price_history
        self.start_date = start_date
        self.end_date = end_date
        self.price_actual = price_actual

    def display_price_history(self):
        print(f"ID: {self.id_price_history}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print(f"Price Actual: {self.price_actual}")


class ProductTest:
    def __init__(self, prod_id, prod_name, prod_ref, release_date, prod_description):
        self._prod_id = prod_id
        self._prod_name = prod_name
        self._prod_ref = prod_ref
        self._release_date = release_date
        self._prod_description = prod_description
        self._prod_key_words = []
        self._prod_ratings = []

    class Admin:
        def __init__(self, inventory):
            self.inventory = inventory

        def add_product(self, product):
            self.inventory.add_product(product)

        def get_product(self, prod_id):
            return self.inventory.get_product(prod_id)

        def update_product(self, prod_id, new_product):
            return self.inventory.update_product(prod_id, new_product)

        def delete_product(self, prod_id):
            return self.inventory.delete_product(prod_id)

        def update_price_history(self, price_history, new_price):
            price_history.price_actual = new_price

        def display_inventory(self):
            for product in self.inventory.products:
                print(product)
    @property
    def prod_id(self):
        return self._prod_id

    @prod_id.setter
    def prod_id(self, value):
        self._prod_id = value

    @property
    def prod_name(self):
        return self._prod_name

    @prod_name.setter
    def prod_name(self, value):
        self._prod_name = value

    @property
    def prod_ref(self):
        return self._prod_ref

    @prod_ref.setter
    def prod_ref(self, value):
        self._prod_ref = value

    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, value):
        self._release_date = value

    @property
    def prod_description(self):
        return self._prod_description

    @prod_description.setter
    def prod_description(self, value):
        self._prod_description = value

    @property
    def prod_key_words(self):
        return self._prod_key_words

    @prod_key_words.setter
    def prod_key_words(self, value):
        self._prod_key_words = value

    @property
    def prod_ratings(self):
        return self._prod_ratings

    @prod_ratings.setter
    def prod_ratings(self, value):
        self._prod_ratings = value

    def __str__(self) -> str:
        return f"ID del producto: {self.prod_id}\nNombre del producto: {self.prod_name}\nReferencia del producto: {self.prod_ref}\nFecha de lanzamiento del producto: {self.release_date}\nDescripcion del producto: {self.prod_description}\nPalabras claves del producto: {self.prod_key_words}\nCalificaciones del producto: {self.prod_ratings}"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_product(self, prod_id):
        for product in self.products:
            if str(product.prod_id) == str(prod_id):  # Convierte ambos ID a cadenas
                return product
        print(f'Producto con ID {prod_id} no encontrado en el inventario')
        return None

    def update_product(self, prod_id, new_product):
        for i, product in enumerate(self.products):
            if str(product.prod_id) == str(prod_id):  # Convierte ambos ID a cadenas
                self.products[i] = new_product
                return True
        return False

    def delete_product(self, prod_id):
        for i, product in enumerate(self.products):
            if str(product.prod_id) == str(prod_id):  # Convierte ambos ID a cadenas
                del self.products[i]
                return True
        return False
