from project.hero import Hero
from unittest import main, TestCase


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Hero", 1, 100.5, 100.5)
        self.enemy = Hero("Enemy", 1, 50.5, 50.5)

    def test_initialisation_is_correct(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100.5, self.hero.health)
        self.assertEqual(100.5, self.hero.damage)

    def test_battle_method_for_wrong_enemy_input_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))


    def test_battle_method_for_low_hero_health_raises_value_error(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_method_for_low_enemy_health_raises_value_error(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ve.exception))

    def test_battle_method_for_draw_result(self):
        self.hero.health = 50.5
        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)

    def test_battle_method_for_hero_win(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105.5, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_method_for_hero_lose(self):
        self.enemy, self.hero = self.hero, self.enemy
        result = self.hero.battle(self.enemy)
        self.assertEqual(2, self.enemy.level)
        self.assertEqual(55, self.enemy.health)
        self.assertEqual(105.5, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test__str__(self):
        expected_result = f"Hero Hero: 1 lvl\nHealth: 100.5\nDamage: 100.5\n"
        result = str(self.hero)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
