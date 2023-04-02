from project.car.car import Car


class MuscleCar(Car):

    @property
    def limits(self):
        return 250, 450
