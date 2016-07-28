from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
from kivy.uix.button import Button
from kivy.uix.label import Label

class dataVariables(Widget):
    def __init__(self):
        self.subwayA = [0.0, 15.0]
    def update(self, dt):
        if self.subwayA[0] < self.subwayA[1]:
            self.subwayA[0] = self.subwayA[0] + 1.0
        else:
            self.subwayA[0] = 0.0



















class timerWidget(Widget):
    def __init__(self, timeleft, **kwargs):
        # make sure we aren't overriding any important functionality
        super(timerWidget, self).__init__(**kwargs)
        self.timeleft = timeleft[:]

        self.groupList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.angleCounter = 0.0
        self.pieSlices = 5.0
        self.currentPieSlice = 0.0
        self.id = 'counter'

        self.rgb = [0.0,1.0,1.0]
        self.rgbCheck = [True, True, True]



    def resetCanvas(self):
        # print 'reset'
        self.currentPieSlice = 0.0
        self.angleCounter = 0.0
        self.canvas.clear()
        with self.canvas:

            Color(0.0, 1.0, 0.0)
            Ellipse(pos=(350, 350), size=(200, 200), group='a', angle_start=0, angle_end = 10)

        self.angleCounter = 1.0
        self.timeleft[0] = 0.0
        self.rgb = [0.0,1.0,1.0]
        self.rgbCheck = [True, True, True]

    def createEllipse(self):
        self.currentPieSlice = self.currentPieSlice + 1.0
        if self.currentPieSlice <= self.pieSlices/3.0:
            print 'one'
            if self.rgbCheck[2] == True:
                self.rgbCheck[2] = False
            else:
                self.rgb[2] = self.rgb[2] - ((1.0) / (self.pieSlices/3.0))
        elif self.currentPieSlice > self.pieSlices/3.0 and self.currentPieSlice <= self.pieSlices/3.0*2:
            print 'two '
            self.rgb[2] = 0.0
            #self.rgb[1] = self.rgb[1] - ((1.0) / (self.pieSlices/3.0))
            self.rgb[0] = self.rgb[0] + ((1.0) / (self.pieSlices/3.0))
        elif self.currentPieSlice >= self.pieSlices/3.0*2:
            print 'three '
            self.rgb[2] = 0.0
            self.rgb[0] = 1.0
            self.rgb[1] = self.rgb[1] - ((1.0) / (self.pieSlices/3.0))
                #self.rgb[0] = self.rgb[0] + ((1.0) / (self.pieSlices/3.0))

        print self.rgb
        with self.canvas:
            Color(self.rgb[0], self.rgb[1], self.rgb[2])
            Ellipse(pos=(350, 350), size=(200, 200), group=self.groupList[int(self.currentPieSlice)], angle_start=self.angleCounter, angle_end=self.angleCounter)

    def update(self, dt):
        # print 'count' + str(self.angleCounter)
        # print 'check' + str(self.currentPieSlice)
        #print 360.0 / 60.0 * self.timeleft
        #360/self.timeleft[1]*60
        #self.timeleft[0] = self.timeleft[0] + 1/60

        self.timeleft[0] = (self.timeleft[0]) + (360/self.timeleft[1]/60)

        if self.currentPieSlice > self.pieSlices:
            self.resetCanvas()
        elif self.angleCounter == 0:
            self.resetCanvas()
        else:
            #self.angleCounter = self.angleCounter + 1
            #self.angleCounter = 360/self.timeleft[1]*self.timeleft[0]
            self.angleCounter = self.timeleft[0]
            #print self.angleCounter
        currentGroup = self.groupList[int(self.currentPieSlice)]
        for i in self.canvas.get_group(currentGroup):
            if 'Ellipse' in str(type(i)):
                # print currentGroup
                # print self.canvas.get_group(currentGroup)[1]
                angle = self.canvas.get_group(currentGroup)[1].angle_end
                if angle < 360/self.pieSlices*self.currentPieSlice:
                    self.canvas.get_group(currentGroup)[1].angle_end = self.angleCounter
                else:
                    self.canvas.get_group(currentGroup)[1].angle_end = self.angleCounter
                    self.createEllipse()

        with self.canvas:
            Color(0, 0, 0)
            Ellipse(pos=(360, 360), size=(180, 180), group='qz', angle_start=0, angle_end=360)

    def updateTimer(self, timeleft, dt):
        self.timeleft[0] = 360/timeleft[1]*timeleft[0]













class clockText(Widget):
    def __init__(self, timeleft, **kwargs):
        # make sure we aren't overriding any important functionality
        super(clockText, self).__init__(**kwargs)
        self.timeleft = timeleft
        self.add_widget(Label( text=str(self.timeleft),pos=(350,350)))
        self.id = 'label'
    def update(self, timeleft, dt):
        for i in self.children:
            i.text=str(timeleft)











class windowWidget(Widget):
    def __init__(self, timeleft, **kwargs):
        super(windowWidget, self).__init__(**kwargs)
        self.timeleft = timeleft

        self.add_widget(timerWidget(self.timeleft.subwayA))
        self.add_widget(clockText(self.timeleft.subwayA))




    def update(self, dt):
        # print self.timeleft.subwayA
        for i in self.children:
            if i.id == 'counter':
                i.update(dt)
            if i.id == 'label':
                i.update(self.timeleft.subwayA,dt)

    def updateTimers(self, dt):
        for i in self.children:
            if i.id == 'counter':
                i.updateTimer(self.timeleft.subwayA, dt)



class GfxApp(App):
    def build(self):
        data = dataVariables()
        Clock.schedule_interval(data.update, 1)
        gWindow = windowWidget(data)
        Clock.schedule_interval(gWindow.update, 1/60)
        Clock.schedule_interval(gWindow.updateTimers, 3)
        return gWindow


if __name__ == '__main__':
    GfxApp().run()
