from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Line, Rectangle

class PongGame(Widget):

    def __init__(self, **kwargs):
        super(PongGame, self).__init__(**kwargs)
        with self.canvas:
            Rectangle(pos=(self.center_x,0), size=(10, self.height))
            Label(font_size=70, center_x=(self.width/4), top=0, text="0")
            Label(font_size=70, center_x=self.width*0.75, top=0, text="0")


class MainApp(App):

    def build(self):
        return PongGame()

if __name__ == "__main__":
    MainApp().run()