class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product_obj):
        self.products.append(product_obj)

    def find(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        product_for_remove = self.find(product_name)
        if product_for_remove:
            self.products.remove(product_for_remove)

    def __repr__(self):
        message = '\n'.join(f"{p}: {p.quantity}" for p in self.products)
        return message
