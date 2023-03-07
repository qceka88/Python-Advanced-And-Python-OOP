class Room:

    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, number_of_guests: int):
        if self.is_taken or self.capacity < number_of_guests:
            return f"Room number {self.number} cannot be taken"

        self.is_taken = True
        self.guests = number_of_guests

    def free_room(self):
        if not self.is_taken:
            return f"Room number {self.number} is not taken"

        self.is_taken = False
        self.guests = 0
