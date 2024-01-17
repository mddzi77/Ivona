from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from .FileRead import handle_dropfile
from kivy.uix.dropdown import DropDown
from kivy.properties import ObjectProperty
import pandas as pd

Builder.load_file('Screens/MainScreen/MainScreenLayout.kv')


# Window.size = (1000, 100)

class MainScreen(Screen):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        Window.bind(on_dropfile=lambda window, file_path: handle_dropfile(window, file_path, self.ids.text_input))

    def open_new_profile(self, button):
        print("New Profile")
