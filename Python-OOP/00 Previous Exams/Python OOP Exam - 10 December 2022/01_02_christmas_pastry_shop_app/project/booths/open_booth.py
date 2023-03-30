from project.booths.booth import Booth


class OpenBooth(Booth):

    @property
    def single_price(self):
        return 2.50
