from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.clock import Clock

class RootWidget(Widget):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)

        # let's add a Widget to this layout
        self.add_widget(
            Button(
                text="Hello World",
                size_hint=(.5, .5),
                pos_hint={'center_x': .5, 'center_y': .5},
                id='asd'))
        #with self.canvas:
    def update(self, dt):
        for i in self.children:
            print i.ids


class MainApp(App):

    def build(self):
        rWidget = RootWidget()
        Clock.schedule_interval(rWidget.update, 0.1)
        return rWidget




if __name__ == '__main__':
    MainApp().run()
