from django.db import models
from datetime import date


class ProductStock:
    def __init__(self, sku_product, current_product_stock, update_stock_date, expiration_stock_date):
        self._sku_product = sku_product
        self._current_product_stock = current_product_stock
        self._update_stock_date = update_stock_date
        self._expiration_stock_date = expiration_stock_date

    @property
    def sku_product(self):
        return self._sku_product

    @property
    def current_product_stock(self):
        return self._current_product_stock

    @property
    def update_stock_date(self):
        return self._update_stock_date

    @property
    def expiration_stock_date(self):
        return self._expiration_stock_date

    @sku_product.setter
    def sku_product(self, new_sku_product):
        self._sku_product = new_sku_product

    @current_product_stock.setter
    def current_product_stock(self, new_current_product_stock):
        self._current_product_stock = new_current_product_stock

    @update_stock_date.setter
    def update_stock_date(self, new_update_stock_date):
        self._update_stock_date = new_update_stock_date

    @expiration_stock_date.setter
    def expiration_stock_date(self, new_expiration_stock_date):
        self._expiration_stock_date = new_expiration_stock_date


class ProductRating:
    def __init__(self, stars_rating, comment_rating, rating_date, rating_update=None):
        self._stars_rating = stars_rating
        self._comment_rating = comment_rating
        self._rating_date = rating_date
        self._rating_update = rating_update

    @property
    def stars_rating(self):
        return self._stars_rating

    @property
    def comment_rating(self):
        return self._comment_rating

    @property
    def rating_date(self):
        return self._rating_date

    @property
    def rating_update(self):
        return self._rating_update

    @stars_rating.setter
    def stars_rating(self, new_stars_rating):
        self._stars_rating = new_stars_rating

    @comment_rating.setter
    def comment_rating(self, new_comment_rating):
        self._comment_rating = new_comment_rating

    @rating_date.setter
    def rating_date(self, new_rating_date):
        self._rating_date = new_rating_date

    @rating_update.setter
    def rating_update(self, new_rating_update):
        self._rating_update = new_rating_update


class ProductCategory:
    def __init__(self, name_category, subcategory, description):
        self._name_category = name_category
        self._subcategory = subcategory
        self._description = description

    @property
    def name_category(self):
        return self._name_category

    @property
    def subcategory(self):
        return self._subcategory

    @property
    def description(self):
        return self._description

    @name_category.setter
    def name_category(self, new_name_category):
        self._name_category = new_name_category

    @subcategory.setter
    def subcategory(self, new_subcategory):
        self._subcategory = new_subcategory

    @description.setter
    def description(self, new_description):
        self._description = new_description


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


class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity=1, size=None, color=None):
        cart_item = {
            'product': product,
            'quantity': quantity,
            'size': size,
            'color': color,
        }
        self.cart_items.append(cart_item)

    def update_cart_item(self, product, new_quantity=None, new_size=None, new_color=None):
        for item in self.cart_items:
            if item['product'] == product:
                if new_quantity is not None:
                    item['quantity'] = new_quantity
                if new_size is not None:
                    item['size'] = new_size
                if new_color is not None:
                    item['color'] = new_color
                return True
        return False

    def display_cart(self):
        for item in self.cart_items:
            product = item['product']
            quantity = item['quantity']
            size = item['size']
            color = item['color']
            print(f"Product: {product.prod_name}, Quantity: {quantity}, Size: {size}, Color: {color}")


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


class ProductBack:
    def __init__(self, product_id, product_tax, product_name, product_reference_model, product_summary_desc,
                 product_release_date, product_creation_date, product_keywords, product_link):
        self._product_id = product_id
        self._product_tax = product_tax
        self._product_name = product_name
        self._product_reference_model = product_reference_model
        self._product_summary_desc = product_summary_desc
        self._product_release_date = product_release_date
        self._product_creation_date = product_creation_date
        self._product_keywords = product_keywords
        self._product_keywords = product_link

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value

    @property
    def product_tax(self):
        return self._product_tax

    @product_tax.setter
    def product_tax(self, value):
        self._product_tax = value

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value

    @property
    def product_reference_model(self):
        return self._product_reference_model

    @product_reference_model.setter
    def product_reference_model(self, value):
        self._product_reference_model = value
    @property
    def product_sumary_desc(self):
        return self._product_summary_desc
    @product_sumary_desc.setter
    def product_sumary_desc(self, value):
        self._product_summary_desc = value

    @property
    def product_release_date(self):
        return self.product_release_date
    @product_release_date.setter
    def product_release_date(self, value):
        self.product_release_date = value

    @property
    def product_creation_date(self):
        return self._product_creation_date

    @product_creation_date.setter
    def product_creation_date(self, value):
        self._product_creation_date = value

    @property
    def product_keywords(self):
        return self.product_keywords

    @product_keywords
    def product_keywords(self, value):
        product_keywords = value
    @property
    def product_keywords(self):
        return self.product_keywords
    @property
    def product_keywords(self, value):
        product_keywords = value

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
