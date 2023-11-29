from unittest import TestCase, main

from List.extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self) -> None:
        self.integer_list = IntegerList(1, 1.5, 2, '2', 3, True, (1, 2, 3), {'a': 1, 'b': 2, 'c': 3})

    def test_correct_init_expected_list_of_integers(self):
        expected_data = [1, 2, 3]

        actual_data = self.integer_list.get_data()

        self.assertEqual(expected_data, actual_data)

    def test_add_method_with_invalid_element_added_expected_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add({1, 2, 3})

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_method_with_correct_element_added_expected_modified_list(self):
        expected_data = [1, 2, 3, 5]

        actual_data = self.integer_list.add(5)

        self.assertEqual(expected_data, actual_data)

    def test_remove_index_method_with_invalid_index_expected_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(3)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_method_with_valid_index_removed_element_and_updated_list_expected(self):
        expected_element = 3
        expected_list = [1, 2]

        actual_element = self.integer_list.remove_index(2)
        actual_list = self.integer_list.get_data()

        self.assertEqual(expected_element, actual_element)
        self.assertEqual(expected_list, actual_list)

    def test_get_method_with_invalid_index_expected_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_method_with_valid_index_returns_element_of_list_on_that_index(self):
        expected_element = 3

        actual_element = self.integer_list.get(2)

        self.assertEqual(expected_element, actual_element)

    def test_insert_method_with_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(3, 1)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_method_with_invalid_element_added_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(0, [1, 2, 4])

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_method_with_valid_index_and_element_expected_modified_list(self):
        expected_list = [1, 2, 5, 3]

        self.integer_list.insert(2, 5)
        actual_list = self.integer_list.get_data()

        self.assertEqual(expected_list, actual_list)

    def test_get_biggest_method_expected_return_of_the_biggest_element(self):
        expected_element = 3

        actual_element = self.integer_list.get_biggest()

        self.assertEqual(expected_element, actual_element)

    def test_get_index_method_expected_index_of_the_element(self):
        expected_index = 0

        actual_index = self.integer_list.get_index(1)

        self.assertEqual(expected_index, actual_index)

    def test_get_index_method_with_element_not_in_the_collection_expected_value_error(self):
        element = 4

        with self.assertRaises(ValueError) as ve:
            self.integer_list.get_index(4)

        self.assertEqual(f'{element} is not in list', str(ve.exception))


if __name__ == '__main__':
    main()
