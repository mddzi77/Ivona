from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from .FileRead import handle_dropfile
from kivy.uix.dropdown import DropDown


Builder.load_file('Screens/MainScreen/MainScreenLayout.kv')


class MainScreen(Screen):

    def __init__(self, tts, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        Window.bind(on_drop_file=self._on_file_drop)
        self.tts = tts

    def _on_file_drop(self, window, file_path, x, y):
        handle_dropfile(window, file_path, self.ids.text_input)
