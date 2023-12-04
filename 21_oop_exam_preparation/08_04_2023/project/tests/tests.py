from unittest import TestCase, main
from project.robots_managing_app import RobotsManagingApp


class TestApp(TestCase):

    def setUp(self) -> None:
        self.app = RobotsManagingApp()

    def test_add_service_invalid_type_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.app.add_service('SomeService', 'Some Name')

        self.assertEqual("Invalid service type!", str(ex.exception))

    def test_add_service_successfully(self):
        result = self.app.add_service('MainService', 'Some name')

        self.assertEqual("MainService is successfully added.", result)

    def test_add_robot_invalid_type_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.app.add_robot('SomeType', 'some name', 'some kind', 100.0)

        self.assertEqual("Invalid robot type!", str(ex.exception))

    def test_add_robot_successfully(self):
        result = self.app.add_robot('MaleRobot', 'some name', 'some kind', 100.0)

        self.assertEqual("MaleRobot is successfully added.", result)

    def test_add_robot_to_service_mismatcing_types(self):
        self.app.add_robot('MaleRobot', 'some robot', 'some kind', 100.0)
        self.app.add_service('SecondaryService', 'some service')

        result = self.app.add_robot_to_service('some robot', 'some service')

        self.assertEqual("Unsuitable service.", result)
        self.assertEqual([], self.app.services[0].robots)
        self.assertEqual(1, len(self.app.robots))

    def test_add_robot_to_service_not_enough_capacity_raises_exception(self):
        """ My error was in this method, so I stopped testing """

        self.app.add_service('SecondaryService', 'some service')
        
        for i in range(15):
            self.app.add_robot('FemaleRobot', str(i), 'very', 100.0)
            self.app.add_robot_to_service(str(i), 'some service')

        self.app.add_robot('FemaleRobot', '15', 'very', 100.0)

        with self.assertRaises(Exception) as ex:
            self.app.add_robot_to_service('15', 'some service')

        self.assertEqual("Not enough capacity for this robot!", str(ex.exception))


if __name__ == '__main__':
    main()
