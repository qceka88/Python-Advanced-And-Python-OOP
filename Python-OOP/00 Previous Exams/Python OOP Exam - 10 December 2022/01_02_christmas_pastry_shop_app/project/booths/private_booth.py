from project.booths.booth import Booth


class PrivateBooth(Booth):

    @property
    def single_price(self):
        return 3.50
