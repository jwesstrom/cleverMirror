from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.animation import Animation



class timerWidget(Widget):
    def __init__(self, x=350, y =350, sizeWH=200, angle=0, id='counter',**kwargs):
        # make sure we aren't overriding any important functionality
        super(timerWidget, self).__init__(**kwargs)
        self.id = id
        self.angle = angle
        self.sizeWH = sizeWH

        self.pos = [x,y]
        #self.size = sizeWH
        Clock.schedule_interval(self.update, 1/25)
        with self.canvas:
            Color(0.0, 1.0, 0.0)
            Ellipse(pos=(self.pos[0], self.pos[1]), size=(self.sizeWH, sizeWH), group='a', angle_start=0, angle_end = 10)

    def update(self, dt, x=None, y=None):



        if self.angle < 360:
            self.angle = self.angle + 1
        else:
            self.angle = 360
        self.canvas.get_group('a')[1].angle_end = self.angle


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
            self.add_widget(timerWidget(div,pos[1],size,aDiv,id+str(i)))

    def update(self, dt):
        for i in self.children:
            if i.angle == 360:
                #self.outAnim(i)
                #i.x = 300
                print i.x


    def outAnim(self, obj):
        anim = Animation(x=50, t='in_quad')
        anim.start(obj)






class GfxApp(App):
    def build(self):
        gWindow = windowWidget()
        Clock.schedule_interval(gWindow.update, 1/30)
        return gWindow


if __name__ == '__main__':
    GfxApp().run()
