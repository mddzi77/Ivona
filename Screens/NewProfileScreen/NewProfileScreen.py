import threading
import time

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
import json

from PredefinedPopups.popup import TextPopup, OkPopup
from Screens.MainScreen.FileRead import get_file_name
from multiprocessing import Process
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from TextToSpeech.tts_handler import TTSHandler
from kivy.uix.popup import Popup

Builder.load_file('Screens/NewProfileScreen/NewProfileScreenLayout.kv')


class NewProfileScreen(Screen):
    def __init__(self, **kwargs):
        super(NewProfileScreen, self).__init__(**kwargs)
        self.popup = TextPopup('Creating profile', 'Loading')
        self.refresh_event = None
        self.refresh_tick = 0

    def add_profile(self, profile_name):
        self.popup.show()
        self.refresh_event = Clock.schedule_interval(lambda dt: self.__popup_refresher(), 0.3)
        threading.Thread(target=self.__clone_thread, args=(profile_name,)).start()

    def __popup_refresher(self):
        self.popup.set_text(Label(text=f"Creating profile{self.refresh_tick * '.'}"))
        self.refresh_tick += 1
        if self.refresh_tick > 3:
            self.refresh_tick = 0

    def __clone_thread(self, profile_name):
        file_name = get_file_name()
        TTSHandler.set_recordings([file_name])
        voice = TTSHandler.clone(profile_name)
        self.__pass_to_json(profile_name, file_name, voice.voice_id)
        Clock.schedule_once(lambda dt: self.__cloning_finished())

    def __cloning_finished(self):
        Clock.unschedule(self.refresh_event)
        self.popup.dismiss()
        self.popup = OkPopup(lambda dt: self.__loading_popup_ok(), 'Ok', 'Profile created')
        self.popup.set_button_size(size_hint=(.2, .5))
        self.popup.show()
        self.manager.get_screen('-main_screen-').ids.profiles_dropdown.refresh_list()

    def __loading_popup_ok(self):
        self.manager.transition.direction = 'right'
        self.manager.current = '-main_screen-'
        self.popup.dismiss()

    def __pass_to_json(self, profile_name, file_name, voice_id):

        new_data = {
            "ProfileName": profile_name,
            "Path": file_name,
            "VoiceID": voice_id
        }

        try:
            with open("Assets/settings.json", "r") as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            existing_data = []

        existing_data['profiles'].append(new_data)

        with open("Assets/settings.json", "w") as f:
            json.dump(existing_data, f, indent=2)


class ListBox(ScrollView):
    values = ListProperty([])

    def __init__(self, **kwargs):
        super(ListBox, self).__init__(**kwargs)
        self.content = GridLayout(cols=1, spacing=10, size_hint=(1, None), height=self.height)
        self.content.bind(minimum_height=self.content.setter('height'))
        self.add_widget(self.content)

    def refresh(self, new_value):
        self.content.clear_widgets()
        self.values.append(new_value)
        for v in self.values:
            self.content.add_widget(Button(text=v, size_hint_y=None, height=40))
