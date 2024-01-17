from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

Builder.load_file('Screens/ProfileScreen/ProfileScreenLayout.kv')


class ProfileGridLayout(Screen):

    def __init__(self, **kwargs):
        super(ProfileGridLayout, self).__init__(**kwargs)

    def function(self):
        pass
