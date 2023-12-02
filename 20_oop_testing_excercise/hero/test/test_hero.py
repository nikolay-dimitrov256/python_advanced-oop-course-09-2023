from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero('Nikolay', 7, 3.0, 5.0)
        self.enemy = Hero('Some enemy', 7, 3.0, 5.0)

    def test_correct_init(self):

        self.assertEqual('Nikolay', self.hero.username)
        self.assertEqual(7, self.hero.level)
        self.assertEqual(3.0, self.hero.health)
        self.assertEqual(5.0, self.hero.damage)

    def test_battle_method_invalid_enemy_username_raises_exception(self):
        self.enemy.username = 'Nikolay'

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_method_with_invalid_hero_health_raises_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

        self.hero.health -= 1

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_method_with_invalid_enemy_health_raises_value_error(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ve.exception))

        self.enemy.health -= 1

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ve.exception))

    def test_battle_method_resulting_in_a_draw(self):

        result = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result)
        self.assertEqual(-32.0, self.hero.health)
        self.assertEqual(-32.0, self.enemy.health)

    def test_battle_method_resulting_in_hero_win(self):
        self.hero.health = 100.0

        result = self.hero.battle(self.enemy)

        self.assertEqual("You win", result)
        self.assertEqual(8, self.hero.level)
        self.assertEqual(70.0, self.hero.health)
        self.assertEqual(10.0, self.hero.damage)

        self.assertEqual(-32.0, self.enemy.health)

    def test_battle_method_resulting_in_hero_loss(self):
        self.enemy.health = 100.0

        result = self.hero.battle(self.enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(8, self.enemy.level)
        self.assertEqual(70.0, self.enemy.health)
        self.assertEqual(10.0, self.enemy.damage)

        self.assertEqual(-32.0, self.hero.health)

    def test_str_method(self):
        expected = f"Hero Nikolay: 7 lvl\nHealth: 3.0\nDamage: 5.0\n"

        self.assertEqual(expected, str(self.hero))


if __name__ == '__main__':
    main()
