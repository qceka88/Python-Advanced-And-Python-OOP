from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    max_mileage = 180.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, CargoVan.max_mileage)

    def drive(self, mileage: float):
        self.battery_level -= round((mileage / CargoVan.max_mileage * 100) + 5)
