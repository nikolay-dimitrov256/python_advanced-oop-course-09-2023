from unittest import TestCase, main

from CarManager.car_manager import Car


class TestCar(TestCase):

    def setUp(self) -> None:
        self.car = Car('Volkswagen', 'Tiguan', 7, 75)

    def test_correct_init(self):
        self.assertEqual('Volkswagen', self.car.make)
        self.assertEqual('Tiguan', self.car.model)
        self.assertEqual(7, self.car.fuel_consumption)
        self.assertEqual(75, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_with_invalid_data_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter_with_invalid_data_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = None

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_setter_with_invalid_data_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_with_invalid_data_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_setter_with_invalid_data_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -3

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_method_with_invalid_data_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_method_with_correct_data_expected_car_fuel_increase(self):
        self.car.refuel(100)

        self.assertEqual(75, self.car.fuel_amount)

    def test_drive_method_with_insufficient_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_method_with_enough_fuel_expected_fuel_decrease(self):
        self.car.refuel(75)

        self.car.drive(100)

        self.assertEqual(68, self.car.fuel_amount)


if __name__ == '__main__':
    main()
