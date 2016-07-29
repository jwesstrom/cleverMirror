from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.properties import BooleanProperty
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
    def __init__(self, angle=0, **kwargs):

        super(timerWidget, self).__init__(**kwargs)

        with self.canvas:
            Color(0.0, 1.0, 0.0)
            self.ellipse = Ellipse(pos=self.pos, size=self.size, group='a', angle_start=0, angle_end = 50)




class windowWidget(EffectWidget):
    def __init__(self, **kwargs):
        super(windowWidget, self).__init__(**kwargs)
        self.add_widget(timerWidget(pos=(300,300), size=(90,90)))
        self.effects = [HorizontalBlurEffect(size=20.0),HorizontalBlurEffect(size=10.0),HorizontalBlurEffect(size=5.0)]



class GfxApp(App):
    def build(self):
        gWindow = windowWidget()
        return gWindow


if __name__ == '__main__':
    GfxApp().run()
