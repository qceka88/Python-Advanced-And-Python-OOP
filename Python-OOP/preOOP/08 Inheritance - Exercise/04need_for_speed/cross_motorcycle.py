from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):

    def drive(self, kilometers):
        if kilometers * self.fuel_consumption <= self.fuel:
            self.fuel -= kilometers * self.fuel_consumption
