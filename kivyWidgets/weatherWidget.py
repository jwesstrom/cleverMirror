# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.image import Image
from kivy.properties import (NumericProperty, BooleanProperty)
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class weatherWidget(Widget):

    def __init__(self, **kwargs):
        super(weatherWidget, self).__init__(**kwargs)
        temperature = '25°'
        #path = 'graphics/renders/cloud1Test_0001.png'
        path = 'graphics/renders/cloud1Test.zip'
        #self.add_widget(Image(source=path,anim_delay=1/25, pos=(400,250), size=(150,150)))
        self.add_widget(Image(source=path,anim_delay=1/25, pos=self.pos, size=(self.size[0]+50,self.size[0]+50)))
        self.add_widget(Label(text='[font=Roboto-Thin]'+temperature+'[/font]', font_size='100sp', markup = True, pos=(self.pos[0]+100,self.pos[1])))







class windowWidget(Widget):
    def __init__(self, **kwargs):
        super(windowWidget, self).__init__(**kwargs)
        self.timerTrigger = ''
        self.trigger = 3
        self.timerList = []
        self.idDict = {}
        x = 30
        y = 350
        pos = [30,350,30]
        op = 1.0
        sizeWH = 100
        for i in range(4):
            x = 100 + (250*i)
            y = 350
            if i == 3:
                op = 0.0
            else:
                op = 1.0 - (0.33*i)
            #
            # if i == 3:
            #     print x
            #     print y
            #     print sizeWH
            self.add_widget(weatherWidget(pos=(x,y), id='c'+str(i), opacity=op,))




    def update(self,dt):
        posDict = {}
        tempDict = {}
        tempList = []
        for i in self.children:
            tempDict = {i.pos[0]:i}
            tempList.append(tempDict)
        b = sorted(tempList)
        for i in b:
            print i
    #     self.outAnim(b[0].key)
    #     Clock.schedule_once(partial(self.nextAnim, b[1]), 0.2)
    #     Clock.schedule_once(partial(self.circulate, b[2]), 0.4)
    #     Clock.schedule_once(partial(self.circulate, i), 0.6)
    #
    #
    #
    # def outAnim(self, obj, *args):
    #     # Animation.cancel_all(self)
    #
    #     anim = Animation(x=obj.pos[0]-100, t='in_back', duration=.3)
    #     anim &=Animation(opacity=0.0, t='in_back', duration=.3)
    #     anim.bind(on_complete=self.newTimeTrigger)
    #     anim.start(obj)
    #
    #
    # def nextAnim(self, obj):
    #     anim = Animation(x=obj.pos[0]-50, t='in_out_back', duration=.3)
    #     anim &=Animation(opacity=obj.opacity+0.33, t='linear', duration=.3)
    #     # anim &=Animation(y=obj.pos[1]+5, t='in_back', duration=.5)
    #     #anim &=Animation(size=(obj.size[0]+5,obj.size[1]+5), t='in_back', duration=.5)
    #     anim.start(obj)
    #
    #
    #
    #














class GfxApp(App):
    def build(self):
        gWindow = windowWidget()
        #gWindow = weatherWidget()
        Clock.schedule_interval(gWindow.update, 5)
        return gWindow


if __name__ == '__main__':
    GfxApp().run()
