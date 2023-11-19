from django.db import models
from datetime import date, datetime

from sqlalchemy import false


class PurchaseInformation:
    def __init__(self, name, description, invoice, currency, amount, tax_base, tax, country, lang, external):
        self.name = name
        self.description = description
        self.invoice = invoice
        self.currency = currency
        self.amount = amount
        self.tax_base = tax_base
        self.tax = tax
        self.country = country
        self.lang = lang
        self.external = false

    @property
    def name(self):
        return self.name

    @property
    def description(self):
        return self.description

    @property
    def invoice(self):
        return self.invoice

    @property
    def currency(self):
        return self.currency

    @property
    def amount(self):
        return self.amount

    @property
    def tax_base(self):
        return self.tax_base

    @property
    def tax(self):
        return self.tax

    @property
    def country(self):
        return self.country

    @property
    def lang(self):
        return self.lang

    @property
    def external(self):
        return self.external

    @external.setter
    def external(self, value):
        self.external = value


class ProductStock:
    def _init_(self, sku_product, current_product_stock, update_stock_date, expiration_stock_date):
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
    def _init_(self, stars_rating, comment_rating, rating_date, rating_update=None):
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
    def _init_(self, name_category, subcategory, description):
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
    def _init_(self, category, name_subcategory, description_subcategory):
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

    def _str_(self):
        return (
            f"Subcategoria: {self.name_subcategory}\n"
            f"Categoria: {self.category.name_category}\n"
            f"Descripcion: {self.description_subcategory}\n"
        )


class ShoppingCart:
    def _init_(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity, size=None, color=None):
        cart_item = {
            'product': product,
            'quantity': quantity,
            'size': size,
            'color': color,
        }
        self.cart_items.append(cart_item)

    def display_cart(self):
        for item in self.cart_items:
            product = item['product']
            quantity = item['quantity']
            size = item['size']
            color = item['color']
            print(f"Product: {product.prod_name}, Quantity: {quantity}, Size: {size}, Color: {color}")

    def total_price(self, code_coupon):
        totalPrice = 0
        IsValidateCoupon = Coupon.validate_Coupon(code_coupon)

        if IsValidateCoupon == True:
            totalPrice = totalPrice - Coupon.discount

        for product in self.cart_items:
            totalPrice += ((PriceHistory.price_actual + ((PriceHistory.tax / 100) * PriceHistory.price_actual))
                           * product['quantity']) + PriceHistory.shipment

        return totalPrice


class Coupon:
    def __init__(self, id_coupon, code_coupon, discount, expiration_date, restrictions):
        self._id_coupon = id_coupon
        self._code_coupon = code_coupon
        self._discount = discount
        self._expiration_date = expiration_date
        self._restriccions = restrictions

    @property
    def id_coupon(self):
        return self._id_coupon

    @property
    def code_coupon(self):
        return self._code_coupon

    @property
    def discount(self):
        return self._discount

    @property
    def expiration_date(self):
        return self._expiration_date

    @property
    def restrictions(self):
        return self._restriccions

    @id_coupon.setter
    def id_coupon(self, value):
        self._id_coupon = value

    @code_coupon.setter
    def code_coupon(self, value):
        self._code_coupon = value

    @discount.setter
    def discount(self, value):
        self._discount = value

    @expiration_date.setter
    def expiration_date(self, value):
        self._expiration_date

    @restrictions.setter
    def restrictions(self, value):
        self._restriccions = value

    def validate_Coupon(self, code_Coupon):
        valid_Coupons = {
            # se deben traer los cupones desde la base de datos
        }

        if (code_Coupon in valid_Coupons):
            coupon = valid_Coupons[code_Coupon]
            date = datetime.date.today()

            if (date <= coupon._expiration_date):
                return True
            else:
                return False
        return False


class PriceHistory:
    def _init_(self, id_price_history, start_date, end_date, price_actual, tax, shipment):
        self.id_price_history = id_price_history
        self.start_date = start_date
        self.end_date = end_date
        self.price_actual = price_actual
        self.tax = tax
        self.shipment = shipment

    def display_price_history(self):
        print(f"ID: {self.id_price_history}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print(f"Price Actual: {self.price_actual}")

    @property
    def price_actual(self):
        return self.price_actual

    @price_actual.setter
    def price_actual(self, value):
        self.price_actual = value

    @property
    def tax(self):
        return self.tax

    @tax.setter
    def tax(self, value):
        self.tax = value

    @property
    def shipment(self):
        return self.shipment

    @shipment.setter
    def shipment(self, value):
        self.shipment = value


class ProductTest:
    def _init_(self, prod_id, prod_name, prod_ref, release_date, prod_description, prod_price):
        self._prod_id = prod_id
        self._prod_name = prod_name
        self._prod_ref = prod_ref
        self._release_date = release_date
        self._prod_description = prod_description
        self._prod_key_words = []
        self._prod_ratings = []
        self._prod_price = prod_price

    class Admin:
        def _init_(self, inventory):
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

    def _str_(self) -> str:
        return f"ID del producto: {self.prod_id}\nNombre del producto: {self.prod_name}\nReferencia del producto: {self.prod_ref}\nFecha de lanzamiento del producto: {self.release_date}\nDescripcion del producto: {self.prod_description}\nPalabras claves del producto: {self.prod_key_words}\nCalificaciones del producto: {self.prod_ratings}"


class Inventory:
    def _init_(self):
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
