from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.properties import ListProperty
from kivy.uix.button import Button
from .FileRead import handle_dropfile
from kivy.metrics import dp
import json

Builder.load_file('Screens/MainScreen/MainScreenLayout.kv')


class MainScreen(Screen):

    def __init__(self, tts, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        Window.bind(on_drop_file=self._on_file_drop)
        self.tts = tts

    def _on_file_drop(self, window, file_path, x, y):
        handle_dropfile(window, file_path, self.ids.text_input)

    def select_voice(self, voice_name):
        try:
            with open("Assets/profiles.json", "r") as f:
                profiles = json.load(f)
                voice_id = ''
                for profile in profiles:
                    if profile["ProfileName"] == voice_name:
                        voice_id = profile["VoiceID"]
                self.tts.set_voice(voice_id)
        except FileNotFoundError as e:
            print(e)

    def generate_audio(self):
        if self.ids.text_input.text == "":
            print("No text to generate")
            return
        try:
            self.tts.set_text(self.ids.text_input.text)
            self.tts.generate()
        except Exception as e:
            print(e)

    def play_audio(self):
        try:
            self.tts.play()
        except Exception as e:
            print(e)


class ProfilesDropDown(Spinner):
    profiles = ListProperty([])

    def __init__(self, **kwargs):
        super(ProfilesDropDown, self).__init__(**kwargs)
        self.text = "Select Profile"
        self.dropdown_cls.max_height = 3 * dp(48)
        self.refresh_list()

    def refresh_list(self):
        self.__get_profiles_from_json()
        self.values.clear()
        for profile in self.profiles:
            self.values.append(profile)

    def __get_profiles_from_json(self):
        self.profiles.clear()
        try:
            with open("Assets/profiles.json", "r") as f:
                existing_data = json.load(f)
                for profile in existing_data:
                    self.profiles.append(profile["ProfileName"])
        except FileNotFoundError as e:
            print(e)
