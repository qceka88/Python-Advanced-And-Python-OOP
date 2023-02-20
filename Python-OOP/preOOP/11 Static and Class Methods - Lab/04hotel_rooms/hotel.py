

class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, number_of_room, people):
        for room in self.rooms:
            if room.number == number_of_room:
                if room.take_room(people) is None:
                    self.guests += people
                break

    def free_room(self, number_of_room):
        for room in self.rooms:
            if room.number == number_of_room:
                people = room.guests
                if room.free_room() is None:
                    self.guests -= people
                break

    def status(self):
        free_rooms = [str(x.number) for x in self.rooms if not x.is_taken]
        taken_rooms = [str(x.number) for x in self.rooms if x.is_taken]
        return f"""Hotel {self.name} has {self.guests} total guests
Free rooms: {', '.join(free_rooms)}
Taken rooms: {', '.join(taken_rooms)}
"""

