import unittest
from games import set_game
from games.set_game import NUMBERS as N, SYMBOLS as SY, SHADINGS as SH, COLORS as C


class Test_set_game(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("[по прежнему лишь имитация настройки]")
        print("v" * 30)

    @classmethod
    def tearDownClass(cls):
        print("v" * 30)
        print("[Подчищаем хвосты]")

    def setUp(self):
        print(f"Подготовка к запуску {self.shortDescription()}")

    def tearDown(self):
        print(f"очистка после прогоа {self.id()}")
        print("-----------")

    def test_generator_work(self):
        self.assertEqual(len(set_game.generate_3card(N, SY, SH, C)), 3)
        with self.assertRaises(ValueError):
            set_game.generate_3card([4, 5], SY, SH, C)
        with self.assertRaises(ValueError):
            set_game.generate_3card(N, ["SY", "sy", "crusifi"], SH, C)
        with self.assertRaises(ValueError):
            set_game.generate_3card(N, SY, ["SY", "sy", "crusifi"], C)
        with self.assertRaises(ValueError):
            set_game.generate_3card(N, SY,SH , ["SY", "sy", "crusifi"])

    def test_check_set(self):
        self.assertIsInstance(set_game.check_set(set_game.generate_3card(N, SY, SH, C)), bool)


if __name__ == "__main__":
    unittest.main()
