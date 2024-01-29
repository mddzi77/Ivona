from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from .FileRead import handle_dropfile

Builder.load_file('Screens/MainScreen/MainScreenLayout.kv')


class MainScreen(Screen):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        Window.bind(on_dropfile=lambda window, file_path: handle_dropfile(window, file_path, self.ids.text_input))
