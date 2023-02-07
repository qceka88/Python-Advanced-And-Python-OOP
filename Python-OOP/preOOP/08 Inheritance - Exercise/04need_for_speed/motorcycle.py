from project.vehicle import Vehicle


class Motorcycle(Vehicle):

    def drive(self, kilometers):
        if kilometers * self.fuel_consumption <= self.fuel:
            self.fuel -= kilometers * self.fuel_consumption
