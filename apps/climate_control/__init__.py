import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

_app_name_ = 'climate_control'

class climate_controlApp(Screen):
    def __init__(self, **kwargs):
        super(climate_controlApp, self).__init__(**kwargs)
        self.name = _app_name_
        self.root = App.get_running_app().root
        self.dir = dirname = os.path.dirname(__file__)

        layout = Builder.load_file("{}/climate.kv".format(self.dir))
        self.add_widget(layout)
