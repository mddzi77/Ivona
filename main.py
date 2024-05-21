from kivy.uix.button import Button
from kivy.uix.label import Label

from Localization.localization import Localization, t
from Screens.MainScreen.MainScreen import MainScreen, ProfilesDropDown
from Screens.NewProfileScreen.NewProfileScreen import NewProfileScreen
from Screens.SettingsScreen.SettingsScreen import SettingsScreen
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
        self.__set_model()

        root = ScreenManager()
        root.add_widget(MainScreen(name='-main_screen-'))
        root.current = '-main_screen-'  # set the current screen to main screen, just in case
        root.add_widget(NewProfileScreen(name='-new_profile_screen-'))
        root.add_widget(SettingsScreen(name='-settings_screen-'))

        return root

    def on_language_change(self):
        main_screen = self.root.get_screen('-main_screen-')
        new_profile_screen = self.root.get_screen('-new_profile_screen-')
        settings_screen = self.root.get_screen('-settings_screen-')

        self.root.remove_widget(main_screen)
        self.root.remove_widget(new_profile_screen)

        self.root.add_widget(MainScreen(name='-main_screen-'))
        self.root.transition.direction = 'left'
        self.root.current = '-main_screen-'
        self.root.add_widget(NewProfileScreen(name='-new_profile_screen-'))

        self.root.remove_widget(settings_screen)
        self.root.add_widget(SettingsScreen(name='-settings_screen-'))

    # for screen in self.root.children:
        #     for widget in screen.walk():
        #         if isinstance(widget, (Label, Button, ProfilesDropDown)):
        #             key = Localization().find_key(widget.text)
        #             widget.text = t(key)

    def __set_model(self):
        with open('Assets/settings.json', 'r') as f:
            data = json.load(f)
            model = data['model']
            if model == ModelType.Default.value:
                TTSHandler.set_model(ModelType.Default)
            elif model == ModelType.ElevenLabs.value:
                TTSHandler.set_model(ModelType.ElevenLabs)


if __name__ == "__main__":
    MyApp().run()
