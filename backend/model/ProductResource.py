class ProductResource:

    def __int__(self, product_length, product_width, product_height, product_weight, product_dimension, product_url_resources):
        self.product_length = product_length
        self.product_width = product_width
        self.product_height = product_height
        self.product_weight = product_weight
        self.product_dimension = product_dimension
        self.product_url_resources = list()

    def product_volume(self):
        return self.product_length * self.product_width * self.product_height

    def product_density(self):
        return self.product_weight / self.product_volume()

    def add_url_resource(self, url):
        self.product_url_resources.append(url)

    def remove_url_resource(self, url):
        self.product_url_resources.remove(url)


