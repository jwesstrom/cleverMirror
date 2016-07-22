from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse

class circle(Widget):
    def __init__(self, posX, **kwargs):
        # make sure we aren't overriding any important functionality
        #super(RootWidget, self).__init__(**kwargs)
        #self.posX = posX

        ellip=Ellipse(pos=(posX,100), size=(100,100))



class RootWidget(Widget):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)

        # let's add a Widget to this layout
        self.add_widget(
            Button(
                text="Hello World",
                size_hint=(.5, .5),
                pos_hint={'center_x': .5, 'center_y': .5}))
        with self.canvas:
            c = circle(50)
            #c.pos = (230, 350)
            c.posX = 15000
            #c.ellip.pos=(210, 350)


class MainApp(App):

    def build(self):
        return RootWidget()




if __name__ == '__main__':
    MainApp().run()
