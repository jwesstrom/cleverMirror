# -*- coding: utf-8 -*-
import datetime
from kivy.app import App
from kivy.uix.widget import Widget
import random
from kivy.clock import Clock
from kivy.properties import StringProperty


class MirrorWindow(Widget):
    time = StringProperty('')
    def update(self, dt):
        self.time = datetime.datetime.today().strftime("%H:%M")

class MirrorApp(App):
    def build(self):
        mirrorWindow = MirrorWindow()
        Clock.schedule_interval(mirrorWindow.update, 1)
        return mirrorWindow


if __name__ == '__main__':
    MirrorApp().run()
