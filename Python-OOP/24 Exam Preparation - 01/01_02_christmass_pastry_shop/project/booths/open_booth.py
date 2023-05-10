from project.booths.booth import Booth


class OpenBooth(Booth):

    @property
    def price(self):
        return 2.50
