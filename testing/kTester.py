# -*- coding: utf-8 -*-
import datetime
from kivy.app import App
from kivy.uix.widget import Widget
import random
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty, ObjectProperty, ReferenceListProperty


class circle(Widget):
    posX = NumericProperty(100)
    posY = NumericProperty(100)
    velocity = ReferenceListProperty(posX, posY)
    def tick(self):
        self.posY = self.posY + 1


class GfxWindow(Widget):
    circle = ObjectProperty(None)
    circle.posX = NumericProperty(500)
    def update(self, dt):
        self.circle.tick()


class GfxApp(App):
    def build(self):
        gfxWindow = GfxWindow()
        Clock.schedule_interval(gfxWindow.update, 1.0/60.0)
        return gfxWindow


if __name__ == '__main__':
    GfxApp().run()
