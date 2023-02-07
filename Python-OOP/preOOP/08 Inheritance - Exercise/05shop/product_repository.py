from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product_obj: Product):
        self.products.append(product_obj)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                break

    def __repr__(self):
        return '\n'.join(f'{product.name}: {product.quantity}' for product in self.products)


# food = Food("apple")
# drink = Drink("water")
# repo = ProductRepository()
# repo.add(food)
# repo.add(drink)
# print(repo.products)
# print(repo.find("water"))
# repo.find("apple").decrease(5)
# print(repo)
