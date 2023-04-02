from project.car.car import Car


class SportsCar(Car):

    @property
    def limits(self):
        return 400, 600

