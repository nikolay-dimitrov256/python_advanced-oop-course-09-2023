from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):

    def setUp(self) -> None:
        self.car = SecondHandCar('Passat', 'sedan', 500_000, 2000.0)

    def test_correct_init(self):
        self.assertEqual('Passat', self.car.model)
        self.assertEqual('sedan', self.car.car_type)
        self.assertEqual(500000, self.car.mileage)
        self.assertEqual(2000.0, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_setter_with_invalid_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1.0

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.9

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_setter_with_invalid_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 99

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price_with_invalid_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(2000.0)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(2001.0)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_with_valid_value_expected_price_update(self):
        expected_message = 'The promotional price has been successfully set.'

        result = self.car.set_promotional_price(1999.0)

        self.assertEqual(1999.0, self.car.price)
        self.assertEqual(expected_message, result)

    def test_need_repair_method_unsuccessfully(self):
        result = self.car.need_repair(1001.0, 'Oil change')

        self.assertEqual('Repair is impossible!', result)

    def test_need_repair_method_successfully_expected_price_and_repairs_update(self):
        result = self.car.need_repair(1000.0, 'Oil change')

        self.assertEqual(3000.0, self.car.price)
        self.assertEqual(['Oil change'], self.car.repairs)
        self.assertEqual('Price has been increased due to repair charges.', result)

        result = self.car.need_repair(1000.0, 'New tires')

        self.assertEqual(4000.0, self.car.price)
        self.assertEqual(['Oil change', 'New tires'], self.car.repairs)
        self.assertEqual('Price has been increased due to repair charges.', result)

    def test_gt_dunder_method_with_different_types(self):
        car2 = SecondHandCar('Peugeot Boxer', 'bus', 500_000, 2000.0)

        result = self.car > car2

        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test_gt_dunder_method_with_same_types_successful_comparison(self):
        car2 = SecondHandCar('Audi 80', 'sedan', 800_000, 500.0)

        self.assertTrue(self.car > car2)
        self.assertFalse(car2 > self.car)
        self.assertFalse(self.car == car2)

    def test_str_method(self):
        expected = "Model Passat | Type sedan | Milage 500000km\nCurrent price: 2000.00 | Number of Repairs: 0"

        self.assertEqual(expected, str(self.car))


if __name__ == '__main__':
    main()
