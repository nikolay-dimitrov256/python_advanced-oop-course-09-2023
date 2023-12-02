from unittest import TestCase, main
from project.trip import Trip


class TestTrip(TestCase):
    def setUp(self) -> None:
        self.trip_test1 = Trip(10_000.0, 1, False)
        self.trip_test2 = Trip(10_000.0, 2, False)
        self.trip_test3 = Trip(10_000.0, 2, True)

    def test_correct_init(self):
        self.assertEqual(10_000.0, self.trip_test1.budget)
        self.assertEqual(1, self.trip_test1.travelers)
        self.assertFalse(self.trip_test1.is_family)
        self.assertTrue(self.trip_test3)

    def test_travelers_setter_invalid_number_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trip_test1.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_setter_with_invalid_data(self):
        self.trip_test1.is_family = True

        self.assertFalse(self.trip_test1.is_family)

    def test_book_trip_method_invalid_destination(self):
        result = self.trip_test3.book_a_trip('Chile')

        self.assertEqual('This destination is not in our offers, please choose a new one!', result)

    def test_book_trip_method_family_discount(self):
        expected_message = 'Successfully booked destination Bulgaria! Your budget left is 9100.00'
        result = self.trip_test3.book_a_trip('Bulgaria')

        self.assertEqual(self.trip_test3.booked_destinations_paid_amounts['Bulgaria'], 900)
        self.assertEqual(self.trip_test3.budget, 9100)
        self.assertEqual(expected_message, result)

    def test_book_trip_method_no_discount(self):
        expected_message = 'Successfully booked destination Bulgaria! Your budget left is 9000.00'
        result = self.trip_test2.book_a_trip('Bulgaria')

        self.assertEqual(self.trip_test2.booked_destinations_paid_amounts['Bulgaria'], 1000)
        self.assertEqual(self.trip_test2.budget, 9000)
        self.assertEqual(expected_message, result)

    def test_book_trip_method_with_insufficient_budget(self):
        result = self.trip_test2.book_a_trip('Brazil')

        self.assertEqual('Your budget is not enough!', result)

    def test_booking_status_without_bookings(self):
        result = self.trip_test2.booking_status()

        self.assertEqual('No bookings yet. Budget: 10000.00', result)

    def test_booking_status_with_bookings(self):
        self.trip_test1.book_a_trip('Australia')
        self.trip_test1.book_a_trip('Bulgaria')

        expected_message = '''Booked Destination: Australia
Paid Amount: 5700.00
Booked Destination: Bulgaria
Paid Amount: 500.00
Number of Travelers: 1
Budget Left: 3800.00'''

        self.assertEqual(expected_message, self.trip_test1.booking_status())


if __name__ == '__main__':
    main()
