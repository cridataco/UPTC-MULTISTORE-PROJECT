class ProductStock:
    def __init__(self, sku_product, current_product_stock, update_stock_date, expiration_stock_date):
        self._sku_product = sku_product
        self._current_product_stock = current_product_stock
        self._update_stock_date = update_stock_date
        self._expiration_stock_date = expiration_stock_date
