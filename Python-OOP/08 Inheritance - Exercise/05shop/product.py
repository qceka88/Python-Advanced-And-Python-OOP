class Product:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    # qty small form of  quantity
    def decrease(self, qty):
        if self.quantity >= qty:
            self.quantity -= qty

    # qty small form of  quantity
    def increase(self, qty):
        self.quantity += qty

    def __repr__(self):
        return self.name
