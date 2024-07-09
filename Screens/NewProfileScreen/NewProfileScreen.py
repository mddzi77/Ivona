import os
import threading

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
import json

from CustomUI.popup import TextPopup, OkPopup
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from TextToSpeech.tts_handler import TTSHandler
from Localization.localization import t

Builder.load_file('Screens/NewProfileScreen/NewProfileScreenLayout.kv')


class NewProfileScreen(Screen):
    def __init__(self, **kwargs):
        super(NewProfileScreen, self).__init__(**kwargs)
        Window.bind(on_drop_file=self.handle_dropfile)
        self.popup = TextPopup(t('creating_profile'), t('loading'))
        self.refresh_event = None
        self.refresh_tick = 0
        self.file_name = ''
        self.__err_msg = ''

    def handle_dropfile(self, window: Window, file_path, x, y):
        file_extension = os.path.splitext(file_path.decode('utf-8'))[1]

        if not self.ids.drop_field.collide_point(*window.mouse_pos):
            return

        if file_extension == '.wav' or file_extension == '.mp3':
            self.file_name = file_path.decode('utf-8').replace('\\', '/')
            self.ids.status_label.text = self.file_name

        Window.raise_window()

    def add_profile(self, profile_name):
        if profile_name is None or profile_name == '' or self.file_name is None or self.file_name == '':
            self.popup = OkPopup(lambda dt: self.__no_data_popup_ok(), title=t('no_profile_data'))
            self.popup.show()
            return
        self.popup = TextPopup(t('creating_profile'), t('loading'))
        self.popup.show()
        self.refresh_event = Clock.schedule_interval(lambda dt: self.__popup_refresher(), 0.3)
        threading.Thread(target=self.__clone_thread, args=(profile_name,)).start()

    def __popup_refresher(self):
        self.popup.set_text(Label(text=t('creating_profile') + self.refresh_tick * '.'))
        self.refresh_tick += 1
        if self.refresh_tick > 3:
            self.refresh_tick = 0

    def __clone_thread(self, profile_name):
        try:
            TTSHandler.set_recordings([self.file_name])
            TTSHandler.clone(profile_name)
            self.__pass_to_json(profile_name, self.file_name)
            Clock.schedule_once(lambda dt: self.__cloning_finished())
        except Exception as err:
            Clock.unschedule(self.refresh_event)
            self.__err_msg = err
            Clock.schedule_once(lambda dt: self.__throw_error())

    def __throw_error(self):
        self.popup.dismiss()
        self.popup = OkPopup(lambda dt: self.__loading_popup_ok(), 'Ok', str(self.__err_msg))
        self.popup.show()
        print(self.__err_msg)

    def __cloning_finished(self):
        Clock.unschedule(self.refresh_event)
        self.popup.dismiss()
        self.popup = OkPopup(lambda dt: self.__loading_popup_ok(), 'Ok', t('profile_created'))
        self.popup.set_button_size(size_hint=(.2, .5))
        self.popup.show()
        self.manager.get_screen('-main_screen-').ids.profiles_dropdown.refresh_list()

    def __loading_popup_ok(self):
        self.manager.transition.direction = 'right'
        self.manager.current = '-main_screen-'
        self.popup.dismiss()

    def __no_data_popup_ok(self):
        self.popup.dismiss()

    def __pass_to_json(self, profile_name, file_name):

        new_data = {
            "ProfileName": profile_name,
            "Path": file_name
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
