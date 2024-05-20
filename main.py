from Screens.MainScreen.MainScreen import MainScreen
from Screens.NewProfileScreen.NewProfileScreen import NewProfileScreen
from Screens.ProfileScreen.ProfileScreen import ProfileGridLayout
from TextToSpeech.tts_handler import *
from kivy.lang import Builder
from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager
import json

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'Width', '800')
Config.set('graphics', 'height', '600')


class MyApp(App):
    icon = 'custom-kivy-icon.png'
    title = 'Basic Application'

    def build(self):
        TTSHandler.set_model(ModelType.ElevenLabs)  # TODO: load it from settings

        root = ScreenManager()
        root.add_widget(MainScreen(name='-main_screen-'))
        root.current = '-main_screen-'  # set the current screen to main screen, just in case
        root.add_widget(NewProfileScreen(name='-new_profile_screen-'))
        root.add_widget(ProfileGridLayout(name='-profile_screen-'))

        return root


if __name__ == "__main__":
    MyApp().run()
