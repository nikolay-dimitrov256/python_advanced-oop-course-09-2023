from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('Sylvester', 'cat', 'Meow')

    def test_correct_init(self):
        self.assertEqual('Sylvester', self.mammal.name)
        self.assertEqual('cat', self.mammal.type)
        self.assertEqual('Meow', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound_method(self):
        expected = 'Sylvester makes Meow'
        actual = self.mammal.make_sound()

        self.assertEqual(expected, actual)

    def test_kingdom_getter(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_info_method(self):
        expected = 'Sylvester is of type cat'
        actual = self.mammal.info()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
