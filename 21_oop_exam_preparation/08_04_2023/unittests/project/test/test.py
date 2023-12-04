from unittest import TestCase, main
from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.player = TennisPlayer('Roger', 30, 100.0)

    def test_correct_inti(self):
        self.assertEqual('Roger', self.player.name)
        self.assertEqual(30, self.player.age)
        self.assertEqual(100.0, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_setter_invalid_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = 'Me'

        self.assertEqual('Name should be more than 2 symbols!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.player.name = 'I'

        self.assertEqual('Name should be more than 2 symbols!', str(ve.exception))

    def test_age_setter_invalid_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17

        self.assertEqual('Players must be at least 18 years of age!', str(ve.exception))

    def test_add_new_win_method(self):
        result = self.player.add_new_win('Wimbeldon')

        self.assertEqual(['Wimbeldon'], self.player.wins)
        self.assertEqual(None, result)

        result = self.player.add_new_win('Wimbeldon')

        self.assertEqual(['Wimbeldon'], self.player.wins)
        self.assertEqual('Wimbeldon has been already added to the list of wins!', result)

    def test_lt_dunder_method(self):
        other_player = TennisPlayer('Novac', 30, 80.0)
        expected = 'Roger is a better player than Novac'
        result = self.player < other_player

        self.assertEqual(expected, result)

        other_player = TennisPlayer('Novac', 30, 101.0)
        expected = 'Novac is a top seeded player and he/she is better than Roger'

        result = self.player < other_player

        self.assertEqual(expected, result)

        other_player = TennisPlayer('Novac', 30, 100.0)
        expected = 'Roger is a better player than Novac'

        result = self.player < other_player

        self.assertEqual(expected, result)

    def test_str_dunder_method(self):
        self.player.add_new_win('Wimbeldon')
        self.player.add_new_win('Roland Garos')
        expected = f'Tennis Player: Roger\nAge: 30\nPoints: 100.0\nTournaments won: Wimbeldon, Roland Garos'

        self.assertEqual(expected, str(self.player))


if __name__ == '__main__':
    main()
