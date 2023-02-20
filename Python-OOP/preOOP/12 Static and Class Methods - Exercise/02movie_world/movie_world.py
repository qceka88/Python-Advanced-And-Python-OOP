class MovieWorld:
    MAX_DVD = 15
    MAX_CUSTOMERS = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.MAX_DVD

    @staticmethod
    def customer_capacity():
        return MovieWorld.MAX_CUSTOMERS

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.MAX_CUSTOMERS:
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.MAX_DVD:
            self.dvds.append(dvd)

    def find_dvd_data(self, dvd_id):
        for dvd_object in self.dvds:
            if dvd_object.id == dvd_id:
                return dvd_object

    def find_customer_data(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer

    def rent_dvd(self, customer_id, dvd_id):
        disk = self.find_dvd_data(dvd_id)
        customer = self.find_customer_data(customer_id)
        if disk in customer.rented_dvds:
            return f"{customer.name} has already rented {disk.name}"
        if disk.is_rented:
            return "DVD is already rented"
        if customer.age < disk.age_restriction:
            return f"{customer.name} should be at least {disk.age_restriction} to rent this movie"
        disk.is_rented = True
        customer.rented_dvds.append(disk)
        return f"{customer.name} has successfully rented {disk.name}"

    def return_dvd(self, customer_id, dvd_id):
        disk = self.find_dvd_data(dvd_id)
        customer = self.find_customer_data(customer_id)
        if disk not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
        disk.is_rented = False
        customer.rented_dvds.remove(disk)
        return f"{customer.name} has successfully returned {disk.name}"

    def __repr__(self):
        customers = '\n'.join(c.__repr__() for c in self.customers)
        dvd = '\n'.join(d.__repr__() for d in self.dvds)
        return customers + '\n' + dvd