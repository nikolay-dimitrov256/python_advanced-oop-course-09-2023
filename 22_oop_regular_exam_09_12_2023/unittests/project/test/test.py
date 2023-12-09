from unittest import TestCase, main
from collections import deque
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self) -> None:
        self.station = RailwayStation("Plovdiv")

    def test_correct_inti(self):
        self.assertEqual("Plovdiv", self.station.name)
        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(deque(), self.station.departure_trains)

    def test_name_setter_invalid_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "Plo"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.station.name = "Pl"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board("some info")

        self.assertEqual(deque(["some info"]), self.station.arrival_trains)

        self.station.new_arrival_on_board("other info")

        self.assertEqual(deque(["some info", "other info"]), self.station.arrival_trains)

    def test_train_has_arrived_unsuccessfully(self):
        self.station.arrival_trains = deque(["some info"])

        result = self.station.train_has_arrived("other info")

        self.assertEqual("There are other trains to arrive before other info.", result)
        self.assertEqual(deque(), self.station.departure_trains)
        self.assertEqual(deque(["some info"]), self.station.arrival_trains)

    def test_train_has_arrived_successfully(self):
        self.station.arrival_trains = deque(["some info"])

        result = self.station.train_has_arrived("some info")

        self.assertEqual("some info is on the platform and will leave in 5 minutes.", result)
        self.assertEqual(deque(["some info"]), self.station.departure_trains)
        self.assertEqual(deque(), self.station.arrival_trains)

    def test_train_has_arrived_pop_from_empty_deque_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.station.train_has_arrived("some info")

        self.assertEqual("pop from an empty deque", str(ie.exception))

    def test_train_has_left_successfully(self):
        self.station.departure_trains = deque(["some info", "other info"])

        result = self.station.train_has_left("some info")

        self.assertTrue(result)
        self.assertEqual(deque(["other info"]), self.station.departure_trains)

    def test_train_has_left_unsuccessfully(self):
        result = self.station.train_has_left("some info")

        self.assertFalse(result)
        self.assertEqual(deque(), self.station.departure_trains)

        self.station.departure_trains = deque(["some info", "other info"])

        result = self.station.train_has_left("other info")

        self.assertFalse(result)
        self.assertEqual(deque(["some info", "other info"]), self.station.departure_trains)


if __name__ == "__main__":
    main()
