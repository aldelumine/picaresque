import os
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label

KIVY_VERSION = "1.11.1"

kivy.require(KIVY_VERSION)


class Game(Widget):

    def __init__(self, game_name, base_path, **kwargs):
        super(Game, self).__init__(**kwargs)

        self._name = game_name
        self.base_path = os.path.abspath(base_path)
        self.kivy_version_str = f"#:kivy {KIVY_VERSION}"

        with open(self.base_path + f"{self.name}.kv", "w", encoding="UTF-8") as kv:
            game_tag = f"<{self.name}>:"
            kv.writelines([self.kivy_version_str + "\n\n", self.name + ":\n\n", game_tag + "\n\n"])

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class MainApp(App):

    def build(self):
        return Label(text="Hello, world!")
