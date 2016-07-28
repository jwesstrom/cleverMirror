from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.properties import BooleanProperty



class timerWidget(Widget):
    def __init__(self, sizeWH=200, angle=0, id='counter',**kwargs):
        # make sure we aren't overriding any important functionality
        outOfTime = BooleanProperty(False)
        super(timerWidget, self).__init__(**kwargs)
        self.id = id
        self.angle = angle
        self.sizeWH = sizeWH
        self.bind(pos=self.update_ellip,size=self.update_ellip)

        self.bind(outOfTime=self.onOutOfTime)
        #self.pos = [x,y]
        #self.size = sizeWH
        Clock.schedule_interval(self.update, 1/25)
        with self.canvas:
            Color(0.0, 1.0, 0.0)
            #Ellipse(pos=self.pos, size=self.size, group='a', angle_start=0, angle_end = 10)
            self.ellip = Ellipse(pos=self.center, size=self.size, group='a', angle_start=0, angle_end = 10)

    def update(self, dt):
        if self.angle < 360:
            self.angle = self.angle + 1
        else:
            self.angle = 360
            self.outOfTime = True
        self.canvas.get_group('a')[1].angle_end = self.angle

    def update_ellip(self, *args):
        self.ellip.pos = self.pos
        self.ellip.size = self.size

    def onOutOfTime(self,instance):
        pass



class windowWidget(Widget):
    def __init__(self, **kwargs):
        super(windowWidget, self).__init__(**kwargs)
        pos = [30,350,90]
        size = 100
        id = 'c'
        aDiv = 360-45
        for i in range(4):
            div = (pos[0]*i) + (pos[2]*i)
            aDiv = (aDiv) - (45*i)
            self.add_widget(timerWidget(pos=(div,350),angle=aDiv))
    def update(self, dt):
        for i in self.children:
            if i.angle == 360:
                i.angle = 380
                print i.angle
                self.outAnim(i)


    def outAnim(self, obj):
        Animation.cancel_all(self)
        anim = Animation(x=150, y=150, t='in_quad')
        anim.start(obj)










class GfxApp(App):
    def build(self):
        gWindow = windowWidget()
        Clock.schedule_interval(gWindow.update, 3)
        return gWindow


if __name__ == '__main__':
    GfxApp().run()
