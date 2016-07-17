# -*- coding: utf-8 -*-
import datetime
from kivy.app import App
from kivy.uix.widget import Widget
import random
from kivy.clock import Clock
from kivy.properties import StringProperty
from webScrape import yrScrape


class MirrorWindow(Widget):
    dayPrint = ['Sön', 'Mån', 'Tis', 'Ons', 'Tors', 'Fre', 'Lör']
    time = StringProperty('')
    day = StringProperty('')
    date = StringProperty('')
    weather1 = StringProperty('')
    weather2 = StringProperty('')
    weather3 = StringProperty('')

    def update(self, dt):
        self.time = datetime.datetime.today().strftime("%H:%M")
        self.day = self.dayPrint[int(datetime.date.today().strftime('%w'))]
        self.date = datetime.date.today().strftime('%y%m%d')
        # for i in range(3):
        #     try:
        #         self.weatheri = yrScrape(i).getWeather()
        #     except IndexError:
        #         print 'asd'
        try:
            self.weather1 = yrScrape(0).getWeather()
        except IndexError:
            print 'asd'
        try:
            self.weather2 = yrScrape(1).getWeather()
        except IndexError:
            print 'asd'
        try:
            self.weather3 = yrScrape(2).getWeather()
        except IndexError:
            print 'asd'

class MirrorApp(App):
    def build(self):
        mirrorWindow = MirrorWindow()
        Clock.schedule_interval(mirrorWindow.update, 1)
        return mirrorWindow


if __name__ == '__main__':
    MirrorApp().run()
