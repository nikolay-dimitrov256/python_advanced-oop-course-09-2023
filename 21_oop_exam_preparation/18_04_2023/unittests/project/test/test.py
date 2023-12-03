from unittest import TestCase, main
from project.robot import Robot


class TestRobot(TestCase):
    ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']

    def setUp(self) -> None:
        self.robot = Robot('P.N.03', 'Military', 1, 100.0)

    def test_correct_inti(self):
        self.assertEqual('P.N.03', self.robot.robot_id)
        self.assertEqual('Military', self.robot.category)
        self.assertEqual(1, self.robot.available_capacity)
        self.assertEqual(100.0, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)
        self.assertEqual(1.5, self.robot.PRICE_INCREMENT)

    def test_category_setter_invalid_data_raises_value_error(self):
        expected = f"Category should be one of '{self.ALLOWED_CATEGORIES}'"

        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'Medical'

        self.assertEqual(expected, str(ve.exception))

    def test_price_setter_invalid_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1

        self.assertEqual('Price cannot be negative!', str(ve.exception))

    def test_upgrade_method_with_existing_component(self):
        self.robot.hardware_upgrades = ['Ryzen 5600']

        result = self.robot.upgrade('Ryzen 5600', 400.0)

        self.assertEqual('Robot P.N.03 was not upgraded.', result)

    def test_upgrade_method_with_new_component_successfully(self):
        result = self.robot.upgrade('Ryzen 5600', 400.0)

        self.assertEqual(['Ryzen 5600'], self.robot.hardware_upgrades)
        self.assertEqual(700.0, self.robot.price)
        self.assertEqual('Robot P.N.03 was upgraded with Ryzen 5600.', result)

    def test_update_method_unsuccessfully(self):
        result = self.robot.update(5.0, 2)

        self.assertEqual('Robot P.N.03 was not updated.', result)

        self.robot.software_updates = [1.0, 2.0, 3.0]

        result = self.robot.update(2.9, 1)

        self.assertEqual('Robot P.N.03 was not updated.', result)

    def test_update_method_successfully(self):
        result = self.robot.update(1.0, 1)

        self.assertEqual([1.0], self.robot.software_updates)
        self.assertEqual(0, self.robot.available_capacity)
        self.assertEqual('Robot P.N.03 was updated to version 1.0.', result)

    def test_gt_dunder_method(self):
        robot2 = Robot('P.N.02', 'Military', 1, 50.0)
        result = self.robot > robot2
        self.assertEqual('Robot with ID P.N.03 is more expensive than Robot with ID P.N.02.', result)

        robot2 = Robot('P.N.02', 'Military', 1, 100.0)
        result = self.robot > robot2
        self.assertEqual('Robot with ID P.N.03 costs equal to Robot with ID P.N.02.', result)

        robot2 = Robot('P.N.02', 'Military', 1, 500.0)
        result = self.robot > robot2
        self.assertEqual('Robot with ID P.N.03 is cheaper than Robot with ID P.N.02.', result)


if __name__ == '__main__':
    main()
