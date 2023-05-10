from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:

    def __init__(self):
        self.bands: [Band] = []
        self.musicians: [Musician] = []
        self.concerts: [Concert] = []

    @property
    def valid_musician(self):
        return {
            "Guitarist": Guitarist,
            "Drummer": Drummer,
            "Singer": Singer
        }

    @staticmethod
    def find_data(value, attribute, some_list):
        for some_object in some_list:
            if getattr(some_object, attribute) == value:
                return some_object

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.valid_musician:
            raise ValueError("Invalid musician type!")

        if self.find_data(name, "name", self.musicians):
            raise Exception(f"{name} is already a musician!")

        new_musician = self.valid_musician[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if self.find_data(name, "name", self.bands):
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self.find_data(place, "place", self.concerts)
        if concert:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.find_data(musician_name, "name", self.musicians)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        band = self.find_data(band_name, "name", self.bands)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.find_data(band_name, "name", self.bands)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = self.find_data(musician_name, "name", self.musicians)
        if musician not in band.members:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self.find_data(band_name, "name", self.bands)

        if len(set(m.__class__.__name__ for m in band.members)) < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = self.find_data(concert_place, "place", self.concerts)
        requirements = concert.required_skills[concert.genre]
        for member in band.members:
            if not set(requirements[member.__class__.__name__]).issubset(set(member.skills)):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")
        else:
            profit = (concert.ticket_price * concert.audience) - concert.expenses
            return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
