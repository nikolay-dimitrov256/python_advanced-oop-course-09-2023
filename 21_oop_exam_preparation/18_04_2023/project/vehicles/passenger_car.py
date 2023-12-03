from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, 450.0)

    def drive(self, mileage: float):
        battery_drain = round(mileage * 100 / self.max_mileage)
        self.battery_level -= battery_drain
