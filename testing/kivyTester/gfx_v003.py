from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
from kivy.uix.button import Button


class GfxWindow(Widget):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(GfxWindow, self).__init__(**kwargs)
        self.groupList = ['a','a','b','c','d','e','f','g','h','i','j','k']
        self.count = 0.0
        self.cCount = 4.0
        self.cCountCheck = 0.0
        self.rgb = 1.0
        # self.add_widget(
        #     Button(
        #         text="Hello World",
        #         size_hint=(.5, .5),
        #         pos_hint={'center_x': .5, 'center_y': .5}))
        with self.canvas:
            Color(0., 1., 0)
            Ellipse(pos=(350, 350), size=(200, 200), group='a', angle_start=0, angle_end = 10)

    def createEllipse(self):
        print 'asdasdasdadas'
        self.cCountCheck = self.cCountCheck + 1
        cDiv = 1-(1.0/(self.cCount+1)*self.cCountCheck)
        with self.canvas:
            Color(0., cDiv, 0)
            Ellipse(pos=(350, 350), size=(200, 200), group=self.groupList[int(self.cCountCheck)], angle_start=self.count, angle_end=self.count)
            #Ellipse(pos=(50, 50), size=(20, 20), group='b', angle_start=self.count, angle_end=self.count)

    # def resetCanvas(self):
    #     self.count = 0.0
    #     self.cCountCheck = 0.0



    def update(self, dt):
        print self.count
        print self.cCountCheck
        if self.count > 360:
            self.cCountCheck = 0.0
            self.count = 0.0
        else:
            self.count = self.count + 1
        currentGroup = self.groupList[int(self.cCountCheck)]
        for i in self.canvas.get_group(currentGroup):
            #self.canvas.get_group(groupItem)[1].angle_end = self.count
            #print self.canvas.get_group(groupItem)[1]
            if 'Ellipse' in str(type(i)):
                angle = self.canvas.get_group(currentGroup)[1].angle_end
                if angle < 360/self.cCount*self.cCountCheck:
                    self.canvas.get_group(currentGroup)[1].angle_end = self.count
                else:
                    self.createEllipse()






class GfxApp(App):
    def build(self):
        gWindow = GfxWindow()
        Clock.schedule_interval(gWindow.update, 0.001)
        return gWindow


if __name__ == '__main__':
    GfxApp().run()
