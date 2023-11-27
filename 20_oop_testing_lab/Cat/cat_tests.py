from unittest import TestCase, main

from Cat.cat import Cat


class CatTests(TestCase):

    def setUp(self) -> None:
        self.cat = Cat('Sylvester')

    def test_eat_method_when_cat_is_fed_raises_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_eat_method_with_hungry_cat_expected_size_increase_fed_and_sleepy_cat(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_sleep_method_with_hungry_cat_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_sleep_method_with_fed_and_sleepy_cat_expected_non_sleepy_cat(self):
        self.cat.eat()

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()
