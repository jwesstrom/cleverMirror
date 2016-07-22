from kivy.base  import  runTouchApp
from kivy.lang  import  Builder

from circle import Circle

from kivy.app import App
from kivy.uix.widget import Widget


class testGame(Widget):
    pass


class testApp(App):
    def build(self):
        return testGame()


if __name__ == '__main__':
    testApp().run()
