from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_correct_init(self):
        expected = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        self.assertEqual(expected, self.toy_store.toy_shelf)

    def test_add_toy_method_invalid_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("H", "toy")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_method_dublicate_toy_raises_exception(self):
        self.toy_store.add_toy("C", "toy")

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("C", "toy")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_method_shelf_taken_raises_exception(self):
        self.toy_store.add_toy("C", "toy")

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("C", "other toy")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_method_successfully(self):
        result = self.toy_store.add_toy("C", "toy")

        self.assertEqual("Toy:toy placed successfully!", result)
        self.assertEqual({
            "A": None,
            "B": None,
            "C": "toy",
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy_store.toy_shelf)

    def test_remove_toy_method_invalid_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("H", 'toy')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_method_wrong_name_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("G", 'toy')

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_method_successfully(self):
        self.toy_store.add_toy("C", "toy")

        result = self.toy_store.remove_toy("C", "toy")

        self.assertEqual("Remove toy:toy successfully!", result)
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy_store.toy_shelf)


if __name__ == "__main__":
    main()
