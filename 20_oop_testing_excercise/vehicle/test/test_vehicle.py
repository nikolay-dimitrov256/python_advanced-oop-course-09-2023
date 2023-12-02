from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(50.0, 140.0)

    def test_correct_init(self):

        self.assertEqual(50.0, self.vehicle.fuel)
        self.assertEqual(50.0, self.vehicle.capacity)
        self.assertEqual(140.0, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

        self.assertIsInstance(self.vehicle.fuel, float)
        self.assertIsInstance(self.vehicle.capacity, float)
        self.assertIsInstance(self.vehicle.horse_power, float)
        self.assertIsInstance(self.vehicle.fuel_consumption, float)

    def test_drive_method_with_insufficient_fuel_raises_exception(self):
        self.vehicle.fuel = 3.5

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(3)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_method_successfully_expected_fuel_decrease(self):
        self.vehicle.drive(4)

        self.assertEqual(45.0, self.vehicle.fuel)

    def test_refuel_method_with_abundant_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_method_successfully_expected_fuel_increase(self):
        self.vehicle.fuel = 5.0

        self.vehicle.refuel(20)

        self.assertEqual(25.0, self.vehicle.fuel)

    def test_str_method(self):
        expected = f"The vehicle has 140.0 horse power with 50.0 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected, str(self.vehicle))


if __name__ == '__main__':
    main()
