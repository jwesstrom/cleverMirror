from kivy.lang          import  Builder
from kivy.uix.widget    import  Widget
from kivy.properties    import  NumericProperty, ObjectProperty, StringProperty,\
                                BooleanProperty, ReferenceListProperty, BoundedNumericProperty,\
                                ListProperty

__all__     = ('Knob',)

Builder.load_string('''
<Circle>
    canvas
        Ellipse:
            pos: self.pos
            size: self.size[0], self.size[1]
            angle_start: 0
            angle_end: 360

''')



class Circle(Widget):
    pass
