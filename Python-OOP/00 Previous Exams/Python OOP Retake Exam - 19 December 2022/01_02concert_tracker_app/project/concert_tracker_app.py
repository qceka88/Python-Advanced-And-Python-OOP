from project.band import Band
from project.band_members.singer import Singer
from project.band_members.guitarist import Guitarist
from project.band_members.drummer import Drummer
from project.concert import Concert


class ConcertTrackerApp:

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    @property
    def valid_musicians(self):
        return {"Guitarist": Guitarist,
                "Drummer": Drummer,
                "Singer": Singer}

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.valid_musicians:
            raise ValueError("Invalid musician type!")

        try:
            musician = next(filter(lambda m: m.name == name, self.musicians))
            raise Exception(f"{musician.name} is already a musician!")

        except StopIteration:
            musician = self.valid_musicians[musician_type](name, age)
            self.musicians.append(musician)

            return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        try:
            band = next(filter(lambda b: b.name == name, self.bands))
            raise Exception(f"{band.name} band is already created!")

        except StopIteration:
            band = Band(name)
            self.bands.append(band)

            return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        try:
            concert = next(filter(lambda c: c.place == place, self.concerts))
            raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")

        except StopIteration:
            concert = Concert(genre, audience, ticket_price, expenses, place)
            self.concerts.append(concert)

            return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            musician = next(filter(lambda m: m.name == musician_name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        for band_data in self.bands:
            if band_data.name == band_name:
                band_data.members.append(musician)
                return f"{musician_name} was added to {band_name}."
        else:
            raise Exception(f"{band_name} isn't a band!")

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        for musician in band.members:
            if musician.name == musician_name:
                band.members.remove(musician)
                return f"{musician_name} was removed from {band_name}."
        else:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

    def start_concert(self, concert_place: str, band_name: str):
        band = next(filter(lambda b: b.name == band_name, self.bands))

        if len(set(m.__class__.__name__ for m in band.members)) < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = next(filter(lambda c: c.place == concert_place, self.concerts))
        requirements = concert.requirements[concert.genre]

        for member in band.members:
            if member.__class__.__name__ == "Singer" and concert.genre == "Jazz" and len(member.skills) != 2:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")
            if not set(member.skills).intersection(set(requirements[member.__class__.__name__])):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        else:
            profit = (concert.audience * concert.ticket_price) - concert.expenses

            return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."
