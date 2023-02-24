from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, Clock






class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    #method to initialize attributes of the created objetc
    # First method to execute when creating an object
    # OOP
    # def __init__([parameters]): 
    # [algorithm]
    def __init__(self, **kwargs):
    #
        super(MainWidget, self).__init__(**kwargs)
        print("INIT Width: " + str(self.width) + "Height: " + str(self.height))
    # Widget needs to be visible before they can receive the focus. To initialize focus, you use the 'on_parent'
    # event. on_open for a popup
    def on_parent(self, widget, parent):

class GalaxyApp(App):

    pass

GalaxyApp().run()