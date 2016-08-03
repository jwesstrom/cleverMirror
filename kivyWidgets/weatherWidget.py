# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse, Rectangle, Line
from kivy.uix.image import Image
from kivy.properties import (NumericProperty, BooleanProperty)
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random
from kivy.graphics import Mesh
from kivy.graphics.texture import Texture
from kivy.uix.effectwidget import EffectWidget, EffectBase

from kivy.uix.effectwidget import (MonochromeEffect,
                                   InvertEffect,
                                   ScanlinesEffect,
                                   ChannelMixEffect,
                                   ScanlinesEffect,
                                   FXAAEffect,
                                   PixelateEffect,
                                   HorizontalBlurEffect,
                                   VerticalBlurEffect)

class weatherWidget(Widget):

    def __init__(self, **kwargs):
        super(weatherWidget, self).__init__(**kwargs)
        temperature = '25°'
        path = 'graphics/renders/cloud1Test_0001.png'
        #path = 'graphics/renders/cloud1Test.zip'
        #self.add_widget(Image(source=path,anim_delay=1/25, pos=(400,250), size=(150,150)))
        # self.pos = (250,250)
        # self.size = (150,150)
        self.add_widget(Image(source=path,anim_delay=1/25, pos=self.pos, size=(self.size[0]+50,self.size[0]+50)))
        self.add_widget(Label(text='[font=Roboto-Thin]'+temperature+'[/font]', font_size='100sp', markup = True, pos=(self.pos[0]+100,self.pos[1])))

        vertices = []
        indices = []
        for i in range(20):
            if i == 0:
                y = 100
            elif i == 19:
                y = 100
            else:
                y = 200+random.randint(1,3)

            x = (10*i) + (50)

            vertices.extend([x, y, 0, 0])
            indices.append(i)

            #‘points’, ‘line_strip’, ‘line_loop’, ‘lines’, ‘triangles’, ‘triangle_strip’ or ‘triangle_fan’

            # create a 64x64 texture, defaults to rgb / ubyte
            texture = Texture.create(size=(64, 64))

            # create 64x64 rgb tab, and fill with values from 0 to 255
            # we'll have a gradient from black to white
            size = 64 * 64 * 3
            buf = [int(x * 255 / size) for x in range(size)]

            # then, convert the array to a ubyte string
            buf = b''.join(map(chr, buf))

            # then blit the buffer
            texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')

            # that's all ! you can use it in your graphics now :)
            # if self is a widget, you can do this

        with self.canvas:
            Mesh(vertices=vertices, indices=indices, mode='triangle_fan')
            #Line(points=[100, 100, 200, 100, 100, 200], width=10)
            Rectangle(texture=texture, pos=self.pos, size=(64, 64))


class fxTest(EffectWidget):
    def __init__(self, **kwargs):
        super(fxTest, self).__init__(**kwargs)
        #effects = [InvertEffect(), HorizontalBlurEffect(size=2.0)]
        self.add_widget(weatherWidget(pos=(250,250),size=(150,150)))
        #self.add_widget(Label(text='asd'))
        #self.effects = [HorizontalBlurEffect(size=10.0)]
        self.effects = [HorizontalBlurEffect(size=50.0),VerticalBlurEffect(size=50.0)]

class GfxApp(App):
    def build(self):
        gWindow = fxTest()
        #gWindow = weatherWidget()
        #Clock.schedule_interval(gWindow.update, 5)
        return gWindow


if __name__ == '__main__':
    GfxApp().run()
