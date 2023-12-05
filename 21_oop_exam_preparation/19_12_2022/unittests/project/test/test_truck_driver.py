from unittest import TestCase, main
from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):

    def setUp(self) -> None:
        self.driver = TruckDriver("Gosho", 10.0)

    def test_correct_init(self):
        self.assertEqual("Gosho", self.driver.name)
        self.assertEqual(10.0, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_setter_invalid_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money -= 1

        self.assertEqual("Gosho went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_method_successfully(self):
        result = self.driver.add_cargo_offer("Plovdiv", 140)

        self.assertEqual({"Plovdiv": 140}, self.driver.available_cargos)
        self.assertEqual("Cargo for 140 to Plovdiv was added as an offer.", result)

    def test_add_cargo_offer_method_invalid_location_raises_exception(self):
        self.driver.add_cargo_offer("Plovdiv", 140)

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Plovdiv", 140)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_drive_best_cargo_offer_successfully(self):
        self.driver.add_cargo_offer("Plovdiv", 20)
        self.driver.add_cargo_offer("Sofia", 140)

        result = self.driver.drive_best_cargo_offer()

        self.assertEqual("Gosho is driving 140 to Sofia.", result)
        self.assertEqual(1400.0, self.driver.earned_money)
        self.assertEqual(140, self.driver.miles)
        # TODO check_for_activities

    def test_drive_best_cargo_offer_no_offers(self):
        result = self.driver.drive_best_cargo_offer()

        self.assertEqual("There are no offers available.", result)

    def test_check_for_activities_method(self):
        self.driver.add_cargo_offer("Oslo", 15000)
        self.driver.drive_best_cargo_offer()

        self.assertEqual(135625.0, self.driver.earned_money)

    def test_repr_dunder_method(self):
        expected = "Gosho has 0 miles behind his back."

        self.assertEqual(expected, repr(self.driver))



if __name__ == "__main__":
    main()
