from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.factory import Factory

class MyWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)

        button = Button(text="Print IDs", id="PrintIDsButton")
        button.bind(on_release=self.print_label)
        self.add_widget(button)

        # crate some labels with defined IDs
        for i in range(5):
            self.add_widget(Button(text=str(i), id="button no: " + str(i)))

        # update moved as per inclement's recommendation
        Clock.schedule_interval(self.update, 1 / 5.0)

    def print_label(self, *args):
        children = self.children[:]
        while children:
            child = children.pop()
            print("{} -> {}".format(child, child.id))
            # Add smiley by ID
            children.extend(child.children)
            if child.id == "PrintIDsButton":
                child.text = child.text + " :)"

    def update(self, *args):
        children = self.children[:]
        while children:
            child = children.pop()
            # remove smiley by ID
            if child.id == "PrintIDsButton":
                child.text  = "Print IDs"

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()
