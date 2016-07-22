# -*- coding: utf-8 -*-
import datetime
from kivy.app import App
from kivy.uix.widget import Widget
import random
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty

class GfxWindow(Widget):
    testStuff = NumericProperty(0)
    def update(self, dt):
        self.testStuff = self.testStuff + 2


class GfxApp(App):
    def build(self):
        gfxWindow = GfxWindow()
        Clock.schedule_interval(gfxWindow.update, 0.1)
        return gfxWindow


if __name__ == '__main__':
    GfxApp().run()
