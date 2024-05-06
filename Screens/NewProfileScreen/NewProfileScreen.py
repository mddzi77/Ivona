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
from Screens.MainScreen.FileRead import get_file_name
from multiprocessing import Process
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from TextToSpeech.tts_handler import TTSHandler
from kivy.uix.popup import Popup

Builder.load_file('Screens/NewProfileScreen/NewProfileScreenLayout.kv')


class NewProfileGridLayout(Screen):
    def __init__(self, **kwargs):
        super(NewProfileGridLayout, self).__init__(**kwargs)
        self.loading_popup = (Popup(
                title='Loading',
                content=Label(text="Loading"),
                size_hint=(None, None),
                size=(300, 180),
                auto_dismiss=False)
            )
        self.modal_view = ModalView(size_hint=(1, 1), background_color=(0, 0, 0, .7))
        self.modal_view.add_widget(self.loading_popup)
        self.clone_p = None
        self.refresh_event = None
        self.refresh_tick = 0

    def add_profile(self, profile_name):
        self.ids.status_label.text = "Creating profile..."
        self.modal_view.open()
        self.refresh_event = Clock.schedule_interval(lambda dt: self.__popup_refresher(), 0.3)
        threading.Thread(target=self.__clone_thread, args=(profile_name,)).start()
        #Clock.schedule_once(lambda dt: self.__clone(profile_name), 2)

    def __popup_refresher(self):
        self.loading_popup.content = Label(text=f"Creating profile{self.refresh_tick * '.'}")
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
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Profile created successfully"))
        layout.add_widget(Button(
                text="OK",
                on_press=lambda x: self.__loading_popup_ok(),
                size_hint=(0.2, 0.2),
                pos_hint={'center_x': 0.5}
            ))
        self.loading_popup.content = layout
        Clock.unschedule(self.refresh_event)

    def __loading_popup_ok(self):
        self.modal_view.dismiss()
        self.manager.transition.direction = 'right'
        self.manager.current = '-main_screen-'

    def __pass_to_json(self, profile_name, file_name, voice_id):

        new_data = {
            "ProfileName": profile_name,
            "Path": file_name,
            "VoiceID": voice_id
        }

        try:
            with open("Assets/profiles.json", "r") as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            existing_data = []

        existing_data.append(new_data)

        with open("Assets/profiles.json", "w") as f:
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
