from kivy.lang          import  Builder
from kivy.uix.widget    import  Widget
from kivy.properties    import  NumericProperty, ObjectProperty, StringProperty,\
                                BooleanProperty, ReferenceListProperty, BoundedNumericProperty,\
                                ListProperty

__all__     = ('Knob',)

Builder.load_string('''
<Circle>
    canvas.before:
        Ellipse:
            pos: self.posX, self.posY
            size: self.sizeWH, self.sizeWH
            angle_start: self.angleS
            angle_end: self.angleE

''')



class Circle(Widget):
    posX = NumericProperty(0)
    posY = NumericProperty(0)
    sizeWH = NumericProperty(0)
    angleS = NumericProperty(0)
    angleE = NumericProperty(0)
