from kivy.base  import  runTouchApp
from kivy.lang  import  Builder

from circle import Circle

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.uix.label import Label


class testGame(Widget):
    def __init__(self, **kwargs):
        super(testGame, self).__init__(**kwargs)
        #self.c = NumericProperty(0)
        testGame.b = self.add_widget(Circle(posX = 100, posY= 20, sizeWH= 50,angleS = 10, angleE = 30, id='bajs' ))
        #testGame.bajss = testGame.b.ids.bajs
        #self.add_widget(Label(text='User Name'))



    def update(self, dt, **kwargs):
        # self.c = self.c + 1
        # print self.c
        #self.b.angleE = self.b.angleE + self.c
        #print self.b.angleE

        # self.add_widget(Circle(posX = 100*self.c, posY= 20*self.c, sizeWH= 50*self.c,angleS = 10*self.c, angle= 80*self.c))
        #print help(self.b)
        # for child in self.children:
        #     #print dir(child)
        #     print vars(child)
        print vars(self.b)
        pass



class testApp(App):
    def build(self):
        game = testGame()
        Clock.schedule_interval(game.update, 1)
        # return game
        return game

if __name__ == '__main__':
    testApp().run()
