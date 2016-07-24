from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock


class GfxWindow(Widget):
    def update(self,dt):
        for i in self.children:
            print i
        #print self.ids['l1'].pos
        print self.canvas.get_group('a')[0].pos
        #self.canvas.get_group('a')[0].pos[0] = 1
        # an_ellipse = self.canvas.get_group('a')[0]
        # an_ellipse.pos = (an_ellipse.pos[0] + 10, an_ellipse.pos[1])


class GfxApp(App):
    def build(self):
        gWindow = GfxWindow()
        Clock.schedule_interval(gWindow.update, 0.1)
        return gWindow


if __name__ == '__main__':
    GfxApp().run()
