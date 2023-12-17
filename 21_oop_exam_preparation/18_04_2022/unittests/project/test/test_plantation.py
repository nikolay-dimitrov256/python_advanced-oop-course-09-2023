from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):

    def setUp(self) -> None:
        self.plantation = Plantation(10)

    def test_correct_init(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_setter_wrong_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_method_successfully(self):
        result = self.plantation.hire_worker("Name")
        expected = "Name successfully hired."

        self.assertEqual(expected, result)
        self.assertEqual(["Name"], self.plantation.workers)

    def test_hire_worker_method_doubled_worker_raises(self):
        self.plantation.hire_worker("Name")

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Name")

        self.assertEqual("Worker already hired!", str(ve.exception))
        self.assertEqual(["Name"], self.plantation.workers)

    def test_len_dunder(self):
        self.assertEqual(0, len(self.plantation))

        self.plantation.plants = {"Gosho": ["Rose", "Tulip"]}

        self.assertEqual(2, len(self.plantation))

    def test_len_add_workers(self):
        self.plantation.hire_worker("Gosho")
        self.plantation.hire_worker("Pesho")
        self.plantation.plants["Gosho"] = ["Rose"]
        self.plantation.plants["Pesho"] = ["Tulip"]

        self.assertEqual(2, len(self.plantation))

    def test_planting_method_invalid_worker_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Name", "Rose")

        self.assertEqual("Worker with name Name is not hired!", str(ve.exception))

    def test_planting_method_full_plantation_raises(self):
        self.plantation.workers = ["Gosho"]
        self.plantation.plants = {"Gosho": []}
        for i in range(10):
            self.plantation.plants["Gosho"].append(str(i))
        expected = {'Gosho': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']}

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Gosho", "Rose")

        self.assertEqual("The plantation is full!", str(ve.exception))
        self.assertEqual(expected, self.plantation.plants)

    def test_planting_method(self):
        self.plantation.workers = ["Gosho", "Pesho"]

        result = self.plantation.planting("Gosho", "Rose")

        self.assertEqual("Gosho planted it's first Rose.", result)
        self.assertEqual({"Gosho": ["Rose"]}, self.plantation.plants)

        result = self.plantation.planting("Gosho", "Tulip")

        self.assertEqual("Gosho planted Tulip.", result)
        self.assertEqual({"Gosho": ["Rose", "Tulip"]}, self.plantation.plants)

        self.plantation.planting("Pesho", "Tulip")
        self.assertEqual({"Gosho": ["Rose", "Tulip"], "Pesho": ["Tulip"]}, self.plantation.plants)

    def test_str_dunder_empty(self):
        expected = "Plantation size: 10\n"

        self.assertEqual(expected, str(self.plantation))

    def test_str_dunder(self):
        self.plantation.workers = ["Gosho", "Pesho"]
        self.plantation.plants = {"Gosho": ["Rose", "Tulip"]}
        expected = "Plantation size: 10\nGosho, Pesho\nGosho planted: Rose, Tulip"

        self.assertEqual(expected, str(self.plantation))

    def test_repr_dunder(self):
        expected = "Size: 10\nWorkers: "

        self.assertEqual(expected, repr(self.plantation))

        self.plantation.workers = ["Gosho", "Pesho"]
        expected = "Size: 10\nWorkers: Gosho, Pesho"

        self.assertEqual(expected, repr(self.plantation))


if __name__ == "__main__":
    main()
