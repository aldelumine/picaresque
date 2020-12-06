import unittest
from picaresque.game import MainApp


class TestGameObject(unittest.TestCase):
    def test_build(self):
        MainApp().build()


if __name__ == "__main__":
    unittest.main()
