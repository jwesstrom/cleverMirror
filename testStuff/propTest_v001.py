from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.properties import NumericProperty


class timerWidget(Widget):
    angle = NumericProperty(30)
    def __init__(self, **kwargs):
        super(timerWidget, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1/25)
        self.bind(angle=self.updateEllipse)
        print self.angle
        with self.canvas:
            Color(0.0, 1.0, 0.0)
            self.ellipse = Ellipse(pos=self.pos, size=self.size, group='a', angle_start=0, angle_end = self.angle)


    def update(self, dt):
        self.angle = self.angle + 1

    def updateEllipse(self, *args):
        self.ellipse.angle_end = self.angle


class windowWidget(Widget):
    def __init__(self, angle=0, **kwargs):
        super(windowWidget, self).__init__(**kwargs)
        self.add_widget(timerWidget())
        self.children[0].bind(angle=self.pTest)

        #self.bind(pos=self.update_ellipse,size=self.update_ellipse)
    def pTest(self, *args):
        print 'asd'



class GfxApp(App):
    def build(self):
        gWindow = windowWidget()

        return gWindow


if __name__ == '__main__':
    GfxApp().run()
