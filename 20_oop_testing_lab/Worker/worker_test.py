from unittest import TestCase, main

from Worker.worker import Worker


class TestWorker(TestCase):

    def setUp(self) -> None:
        self.worker = Worker('George', 1200, 10)

    def test_correct_initialization(self):
        self.assertEqual('George', self.worker.name)
        self.assertEqual(1200, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_method_with_zero_energy_raises_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_method_with_positive_energy_expected_energy_decrease_and_money_increase(self):

        self.worker.work()

        self.assertEqual(1200, self.worker.money)
        self.assertEqual(9, self.worker.energy)

    def test_rest_method_expected_energy_increase(self):
        self.worker.rest()

        self.assertEqual(11, self.worker.energy)

    def test_get_info_method_expected_correct_string(self):
        expected_string = 'George has saved 0 money.'

        actual_string = self.worker.get_info()

        self.assertEqual(expected_string, actual_string)


if __name__ == '__main__':
    main()