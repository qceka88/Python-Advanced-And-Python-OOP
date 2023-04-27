from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    def __init__(self):
        self.users: [User] = []
        self.vehicles: [BaseVehicle] = []
        self.routes: [Route] = []

    @staticmethod
    def find_data(value, attribute, some_list):
        for obj in some_list:
            if getattr(obj, attribute) == value:
                return obj

    @property
    def valid_vehicle(self):
        return {"PassengerCar": PassengerCar,
                "CargoVan": CargoVan,
                }

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if self.find_data(driving_license_number, "driving_license_number", self.users):
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.valid_vehicle:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if self.find_data(license_plate_number, "license_plate_number", self.vehicles):
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = self.valid_vehicle[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point:
                if route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."

                if route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."

                if route.length > length:
                    route.is_locked = True

        new_route = Route(start_point, end_point, length, Route.id_num)
        self.routes.append(new_route)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):

        user = self.find_data(driving_license_number, "driving_license_number", self.users)
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        vehicle = self.find_data(license_plate_number, "license_plate_number", self.vehicles)
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        route = self.find_data(route_id, "route_id", self.routes)
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()
        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        counter = 0
        for n, vehicle in enumerate(sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))):
            if n == count:
                break
            vehicle.change_status()
            vehicle.recharge()
            counter += 1

        return f"{counter} vehicles were successfully repaired!"

    def users_report(self):
        return "*** E-Drive-Rent ***\n" + \
            "\n".join([str(u) for u in sorted(self.users, key=lambda u: -u.rating)])
