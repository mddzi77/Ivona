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


class ProfilesDropDown(Spinner):
    profiles = ListProperty([])

    def __init__(self, **kwargs):
        super(ProfilesDropDown, self).__init__(**kwargs)
        self.text = "Select Profile"
        self.dropdown_cls.max_height = 3 * dp(48)
        self.refresh_list()
        # self.main_button = Button(text='Select Profile', size_hint=(None, None), height=40, width=200)
        # self.main_button.bind(on_release=self.open)
        # self.bind(on_select=lambda instance, x: setattr(self.main_button, 'text', x))

    def refresh_list(self):
        self.__get_profiles_from_json()
        self.values.clear()
        # self.clear_widgets()
        for profile in self.profiles:
            self.values.append(profile)
            # btn = Button(text=profile, size_hint_y=None, height=40)
            # btn.bind(on_release=lambda btn: self.select(btn.text))
            # self.add_widget(btn)

    def __get_profiles_from_json(self):
        self.profiles.clear()
        try:
            with open("Assets/profiles.json", "r") as f:
                existing_data = json.load(f)
                for profile in existing_data:
                    self.profiles.append(profile["ProfileName"])
        except FileNotFoundError as e:
            print(e)
