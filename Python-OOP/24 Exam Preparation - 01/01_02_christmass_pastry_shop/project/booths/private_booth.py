from project.booths.booth import Booth


class PrivateBooth(Booth):

    @property
    def price(self):
        return 3.50

