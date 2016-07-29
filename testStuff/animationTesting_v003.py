from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.properties import (NumericProperty, BooleanProperty)




class timerWidget(Widget):

    angle = NumericProperty(30)
    timesUp = BooleanProperty(False)
    newTime = BooleanProperty(True)

    def __init__(self, **kwargs):
        super(timerWidget, self).__init__(**kwargs)

        self.bind(pos=self.update_ellipse,size=self.update_ellipse,angle=self.update_ellipse)
        Clock.schedule_interval(self.update, 1/25)

        with self.canvas:
            Color(0.0, 1.0, 0.0)
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
                op = 0.1
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
                    print 'timeup'
                    print i.timesUp
                    i.timesUp = True
                    print i.timesUp
                    self.outAnim(i)
                    Clock.schedule_once(self.nextAnimCall, .2)
                    Clock.schedule_once(self.nextAnimCall, .4)
                    Clock.schedule_once(self.nextAnimCall, .6)



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
        # for i in self.children:
        #     if i.opacity == 0.15:
        #         print i.id
        #         if i.timesUp == True:
        #             i.newTime = False
        #             print 'bajs'
        pass



    def outAnimCall(self, dt):
        self.outAnim(self.children[self.trigger])
        if self.trigger > 0:
            self.trigger = self.trigger - 1
        else:
            self.trigger = 3

    def nextAnimCall(self, *args):
        if self.trigger > 0:
            self.trigger = self.trigger - 1
        else:
            self.trigger = 3
        self.nextAnim(self.children[self.trigger])




    def test(self, *args, **kwargs):
        args[1].newTime = False


    def outAnim(self, obj, *args):
        # Animation.cancel_all(self)
        anim = Animation(x=obj.pos[0]-100, t='in_back', duration=.5)
        anim &=Animation(opacity=0.15, t='in_back', duration=.5)
        anim.bind(on_complete=self.test)
        anim.start(obj)


    def nextAnim(self, obj):
        anim = Animation(x=obj.pos[0]-50, t='in_back', duration=.5)
        anim &=Animation(opacity=obj.opacity+0.33, t='linear', duration=.5)
        # anim &=Animation(y=obj.pos[1]+5, t='in_back', duration=.5)
        #anim &=Animation(size=(obj.size[0]+5,obj.size[1]+5), t='in_back', duration=.5)
        anim.start(obj)

    def update(self, dt):
        for i in self.ids:
            print i









class GfxApp(App):
    def build(self):
        gWindow = windowWidget()
        Clock.schedule_interval(gWindow.update, 1)
        return gWindow


if __name__ == '__main__':
    GfxApp().run()
