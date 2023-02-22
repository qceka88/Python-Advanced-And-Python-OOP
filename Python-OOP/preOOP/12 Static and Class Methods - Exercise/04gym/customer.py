class Customer:
    main_id = 0

    def __init__(self, *input_data):
        [self.name,
         self.address,
         self.email
         ] = input_data
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        Customer.main_id += 1
        return Customer.main_id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
