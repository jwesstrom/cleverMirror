from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
from kivy.uix.button import Button


class GfxWindow(Widget):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(GfxWindow, self).__init__(**kwargs)
        # self.add_widget(
        #     Button(
        #         text="Hello World",
        #         size_hint=(.5, .5),
        #         pos_hint={'center_x': .5, 'center_y': .5}))
        with self.canvas:
            Ellipse(pos=(50, 50), size=(20, 20), group='a', uid='22')
            Ellipse(pos=(10, 10), size=(20, 20), group='a')

    def update(self, dt):
        #print self.canvas.get_group('a')[0]
        # for i in self.children:
        #     print i
        # for i in self.canvas.get_group('a'):
        #     print i
        # an_ellipse = self.canvas.get_group('a')[1]
        # an_ellipse2 = self.canvas.get_group('a')[0]
        # an_ellipse.pos = (an_ellipse.pos[0] + 10, an_ellipse.pos[1])
        # #print dir(an_ellipse)
        # print an_ellipse.uid
        # print self.uid
        # pass
        for i in self.canvas.get_group('a'):
            print i.uid


class GfxApp(App):
    def build(self):
        gWindow = GfxWindow()
        Clock.schedule_interval(gWindow.update, 3)
        return gWindow


if __name__ == '__main__':
    GfxApp().run()
