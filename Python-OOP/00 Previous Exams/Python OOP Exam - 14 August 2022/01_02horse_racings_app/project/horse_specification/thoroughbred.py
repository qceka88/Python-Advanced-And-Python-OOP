from project.horse_specification.horse import Horse


class Thoroughbred(Horse):

    @property
    def max_speed(self):
        return 140

    @property
    def gained_speed(self):
        return 3
