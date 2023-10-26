from django.db import models
from datetime import date



#tener en cuenta que esta clase 'SubCategory' depende de ProductCategory para acceder a sus propiedades
class ProductSubcategory:
    def __init__(self, category, name_subcategory, description_subcategory):
        self._category = category
        self._name_subcategory = name_subcategory
        self._description_subcategory = description_subcategory

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    @property
    def name_subcategory(self):
        return self._name_subcategory

    @name_subcategory.setter
    def name_subcategory(self, value):
        self._name_subcategory = value

    @property
    def description_subcategory(self):
        return self._description_subcategory

    @description_subcategory.setter
    def description_subcategory(self, value):
        self._description_subcategory = value

    def __str__(self):
        return (
            f"Subcategoria: {self.name_subcategory}\n"
            f"Categoria: {self.category.name_category}\n"
            f"Descripcion: {self.description_subcategory}\n"
        )

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
