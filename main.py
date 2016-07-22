# -*- coding: utf-8 -*-
import datetime
from kivy.app import App
from kivy.uix.widget import Widget
import random
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty
from webScrape import webScraper




class MirrorWindow(Widget):
    dayPrint = ['Sön', 'Mån', 'Tis', 'Ons', 'Tors', 'Fre', 'Lör']
    secondsAnim = NumericProperty(0)
    minute = NumericProperty(0)
    time = StringProperty('')
    day = StringProperty('')
    date = StringProperty('')
    weather1 = StringProperty('')
    weather2 = StringProperty('')
    weather3 = StringProperty('')
    seconds = StringProperty('')

    def update(self, dt):
        self.time = datetime.datetime.today().strftime("%H:%M")
        self.day = self.dayPrint[int(datetime.date.today().strftime('%w'))]
        self.date = datetime.date.today().strftime('%y%m%d')
        #self.seconds = str (( int (datetime.datetime.today().strftime('%f')) / 1000 ) )
        #self.seconds = ( int (datetime.datetime.today().strftime('%f')) / 1000 )
        self.seconds = str(datetime.datetime.today().strftime('%S'))
        # self.weather1 = (' ').join(webScraper().weather()[0][:3])
        # self.weather2 = (' ').join(webScraper().weather()[1][:3])
        # self.weather3 = (' ').join(webScraper().weather()[2][:3])
        #60 000 000
        if self.secondsAnim < 360:
            self.secondsAnim = self.secondsAnim + 6
        else:
            self.secondsAnim = 0
        #self.minute = int (datetime.datetime.today().strftime('%S') )
        if self.minute < 360:
            self.minute = self.minute + 0.1
        else:
            self.minute = 0.1
class MirrorApp(App):
    def build(self):
        mirrorWindow = MirrorWindow()
        Clock.schedule_interval(mirrorWindow.update, 0.01)
        return mirrorWindow


if __name__ == '__main__':
    MirrorApp().run()
