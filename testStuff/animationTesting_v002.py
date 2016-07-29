from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.properties import (BooleanProperty, NumericPropertie)
from kivy.uix.effectwidget import EffectWidget



class timerWidget(Widget):
    def __init__(self, angle=0, **kwargs):

        super(timerWidget, self).__init__(**kwargs)
        self.angle = angle
        self.done = False
        self.newCycle = True
        self.bind(pos=self.update_ellipse,size=self.update_ellipse)


        Clock.schedule_interval(self.update, 1/25)

        with self.canvas:
            Color(0.0, 1.0, 0.0)
            self.ellipse = Ellipse(pos=self.pos, size=self.size, group='a', angle_start=0, angle_end = 10)

    def update(self, dt):
        if self.angle < 360:
            self.angle = self.angle + 0.1
        else:
            self.angle = 360
            if self.newCycle == True:
                self.newCycle = False
                self.done = True


        self.canvas.get_group('a')[1].angle_end = self.angle

    def update_ellipse(self, *args):
        self.ellipse.pos = self.pos
        self.ellipse.size = self.size








class windowWidget(EffectWidget):
    def __init__(self, **kwargs):
        super(windowWidget, self).__init__(**kwargs)
        self.timerTrigger = ''
        self.trigger = 3
        x = 30
        y = 350
        pos = [30,350,30]
        aDiv = 360-45
        op = 1.0
        sizeWH = 100
        for i in range(4):
            x = 100 + (50*i) + (5*i)
            y = 350 + ((10*i)/2)
            aDiv = (aDiv) - (45*i)
            sizeWH = 100 - (10*i)
            if i == 3:
                op = 0.0
            else:
                op = 1.0 - (0.33*i)
            print op

            self.add_widget(timerWidget())


    def update(self, dt):
        for i in self.children:
            #print i.opacity
            if i.done == True:
                i.done = False
                self.outAnim(i)
                Clock.schedule_once(self.my_callback, .2)
                Clock.schedule_once(self.my_callback, .4)
                Clock.schedule_once(self.my_callback, .6)


    # def moveAllChildren(self):
    #     for i in self.children


    def outAnim(self, obj):
        # Animation.cancel_all(self)
        anim = Animation(x=obj.pos[0]-100, t='in_back', duration=.5)
        anim &=Animation(opacity=0, t='in_back', duration=.5)
        anim.start(obj)


    def nextAnim(self, obj):
        anim = Animation(x=obj.pos[0]-105, t='in_back', duration=.5)
        anim &=Animation(opacity=obj.opacity+0.33, t='linear', duration=.5)
        anim &=Animation(y=obj.pos[1]+5, t='in_back', duration=.5)
        anim &=Animation(size=(obj.size[0]+5,obj.size[1]+5), t='in_back', duration=.5)
        anim.start(obj)

    def my_callback(self, dt):
        self.trigger = self.trigger - 1
        self.nextAnim(self.children[self.trigger])
        print self.trigger









class GfxApp(App):
    def build(self):
        gWindow = windowWidget()
        Clock.schedule_interval(gWindow.update, 1/30)
        return gWindow


if __name__ == '__main__':
    GfxApp().run()
