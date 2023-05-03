from project.hero import Hero
from unittest import main, TestCase


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("Druid", 10, 55.5, 100.5)
        self.enemy = Hero("Amazon", 1, 20.5, 50.5)

    def test_initialisation_is_correct(self):
        self.assertEqual("Druid", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(55.5, self.hero.health)
        self.assertEqual(100.5, self.hero.damage)

    def test_battle_same_name_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_insufficient_health(self):
        self.hero.health = 0

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_draw_result(self):
        test_hero = Hero("Amazon", 10, 55.5, 100.5)
        result = self.hero.battle(test_hero)

        self.assertEqual("Draw", result)

    def test_battle_hero_win(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual("You win", result)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(10, self.hero.health)
        self.assertEqual(105.5, self.hero.damage)

    def test_battle_enemy_win(self):
        self.hero, self.enemy = self.enemy, self.hero

        result = self.hero.battle(self.enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(11, self.enemy.level)
        self.assertEqual(10, self.enemy.health)
        self.assertEqual(105.5, self.enemy.damage)

    def test__str__(self):
        expected_result = f"Hero Druid: 10 lvl\nHealth: 55.5\nDamage: 100.5\n"
        result = str(self.hero)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
