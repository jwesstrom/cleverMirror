from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.properties import (NumericProperty, BooleanProperty)
from functools import partial
from kivy.uix.effectwidget import EffectWidget
from kivy.uix.effectwidget import (MonochromeEffect,
                                   InvertEffect,
                                   ScanlinesEffect,
                                   ChannelMixEffect,
                                   ScanlinesEffect,
                                   FXAAEffect,
                                   PixelateEffect,
                                   HorizontalBlurEffect,
                                   VerticalBlurEffect)







class timerWidget(Widget):

    angle = NumericProperty(30)
    timesUp = BooleanProperty(False)
    newTime = BooleanProperty(True)

    def __init__(self, **kwargs):
        super(timerWidget, self).__init__(**kwargs)

        self.bind(pos=self.update_ellipse,size=self.update_ellipse,angle=self.update_ellipse)
        Clock.schedule_interval(self.update, 1/25)

        with self.canvas:
            Color(1.0, 1.0, 1.0)
            self.ellipse = Ellipse(pos=self.pos, size=self.size, group='a', angle_start=0, angle_end = self.angle)


    def update(self, dt):
        if self.angle < 360:
            self.angle = self.angle + .5
        else:
            self.angle = 360

    def update_ellipse(self, *args):
        self.ellipse.pos = self.pos
        self.ellipse.size = self.size
        self.ellipse.angle_end = self.angle






class windowWidget(Widget):
    def __init__(self, angle=0, **kwargs):
        super(windowWidget, self).__init__(**kwargs)
        self.timerTrigger = ''
        self.trigger = 3
        self.timerList = []
        self.idDict = {}
        x = 30
        y = 350
        pos = [30,350,30]
        aDiv = 360-45
        op = 1.0
        sizeWH = 100
        for i in range(4):
            x = 100 + (50*i)
            y = 350
            aDiv = (aDiv) - (45*i)
            sizeWH = 100 - (10*i)
            # x = self.ellipsePivot(x,y,sizeWH)[0]
            # y = self.ellipsePivot(x,y,sizeWH)[1]
            if i == 3:
                op = 0.0
            else:
                op = 1.0 - (0.33*i)
            #
            # if i == 3:
            #     print x
            #     print y
            #     print sizeWH
            self.add_widget(timerWidget(angle=aDiv, pos=(x,y), id='c'+str(i), opacity=op,))

        for i in self.children:
            i.bind(angle=self.angleTest,timesUp=self.timesUp,newTime=self.newTime, opacity=self.opTest)
            tempDict = {i.id:i}
            self.idDict.update(tempDict)


    def ellipsePivot(self, x,y,size):
        pivot = [x+(size/2), y+(size/2)]
        return pivot


    def angleTest(self, *args):
        for i in self.children:
            if i.angle == 360:
                if i.timesUp == False:
                    i.timesUp = True
                    self.outAnim(i)

                    Clock.schedule_once(partial(self.circulate, i, 0), 0.2)
                    Clock.schedule_once(partial(self.circulate, i, 1), 0.4)
                    Clock.schedule_once(partial(self.circulate, i, 2), 0.6)


    def circulate(self, obj, order, *args):
        posDict = {}
        tempDict = {}
        tempList = []
        for i in self.children:
            if i.id != obj.id:
                tempDict = {i.pos[0]:i}
                tempList.append(tempDict)
        b = sorted(tempList)[order]
        a = b.keys()[0]
        self.nextAnim (b[a])






    def newTimeTrigger(self, *args, **kwargs):
        args[1].newTime = False


    def outAnim(self, obj, *args):
        # Animation.cancel_all(self)

        anim = Animation(x=obj.pos[0]-100, t='in_back', duration=.3)
        anim &=Animation(opacity=0.0, t='in_back', duration=.3)
        anim.bind(on_complete=self.newTimeTrigger)
        anim.start(obj)







    def nextAnim(self, obj):
        anim = Animation(x=obj.pos[0]-50, t='in_out_back', duration=.3)
        anim &=Animation(opacity=obj.opacity+0.33, t='linear', duration=.3)
        # anim &=Animation(y=obj.pos[1]+5, t='in_back', duration=.5)
        #anim &=Animation(size=(obj.size[0]+5,obj.size[1]+5), t='in_back', duration=.5)
        anim.start(obj)


    def newTime(self, *args):
        for i in self.children:
            if i.newTime == False:
                    i.newTime = True
                    i.timesUp = False
                    i.angle = 0
                    i.timesUp = False
                    i.pos = (265,350)
                    # i.size = (70,70)







    def timesUp(self, *args):
        pass

    def opTest(self, *args):
        pass






















class GfxApp(App):
    def build(self):
        gWindow = windowWidget()
        return gWindow


if __name__ == '__main__':
    GfxApp().run()
