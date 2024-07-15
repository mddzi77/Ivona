import os
import threading

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.spinner import Spinner
from kivy.properties import ListProperty
from kivy.uix.button import Button
from CustomUI.popup import TextPopup
from CustomUI.popup import OkPopup
from FileRead.file_read import read_pdf

from kivy.metrics import dp
import json

from TextToSpeech.tts_handler import TTSHandler
from Localization.localization import t
from PathChooser.FileChooserPopup import FileChooserPopup
Builder.load_file('Screens/MainScreen/MainScreenLayout.kv')


class MainScreen(Screen):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        Window.bind(on_drop_file=self.handle_dropfile)
        self.popup = TextPopup(t('generating'), t('loading'))
        self.refresh_event = None
        self.refresh_tick = 0
        self.profile_selected = False
        self.audio_generated = False
        self.selected_path = None
        self.popup_inf = OkPopup(lambda dt: self.__loading_popup_ok(), 'Ok', t('info'))
        self.error_popup = OkPopup(lambda dt: self.__loading_popup_ok(), 'Ok', 'Error')
        self.i = True

    def handle_dropfile(self, window: Window, file_path, x, y):
        file_extension = os.path.splitext(file_path.decode('utf-8'))[1]

        if file_extension == '.wav' or file_extension == '.mp3':
            global file_name
            file_name = file_path.decode('utf-8').replace('\\', '/')
            return

        try:
            if self.ids.text_input.collide_point(*window.mouse_pos):
                read_pdf(file_path, self.ids.text_input)
        except Exception as e:
            self.ids.text_input.text = f"Error: {str(e)}"

        Window.raise_window()

    def __loading_popup_ok(self):
        self.popup_inf.dismiss()

    def throw_information(self):
        if self.i:
            self.popup_inf.show()
            self.i = False

    def select_voice(self, voice_name):
        try:
            with open("Assets/settings.json", "r") as f:
                profiles = json.load(f)['profiles']
                TTSHandler.set_voice(voice_name)
                self.profile_selected = True
        except FileNotFoundError as e:
            print(e)

    def generate_play_button(self):
        if self.audio_generated:
            self.play_audio()
        else:
            self.generate_audio()

    def generate_audio(self):
        if self.ids.text_input.text == "":
            self.error_popup = OkPopup(lambda x: self.error_popup.dismiss(), 'Ok', t('no_text_to_gen'))
            return
        elif not self.profile_selected:
            self.error_popup = OkPopup(lambda x: self.error_popup.dismiss(), 'Ok', t('no_profile_selected'))
            return
        self.popup.show()
        self.refresh_event = Clock.schedule_interval(lambda dt: self.__popup_refresher(), 0.3)
        threading.Thread(target=self.__generate_thread).start()

    def play_audio(self):
        try:
            TTSHandler.play()
        except Exception as e:
            print(e)

    def save_file(self):
        file_chooser_popup = FileChooserPopup(callback=self.finalize_save)
        file_chooser_popup.open()

    def finalize_save(self, path):
        self.selected_path = path
        if self.selected_path:
            try:
                TTSHandler.save(self.selected_path)
                print(f'File saved to {self.selected_path}')
            except Exception as e:
                print(e)

    def stop_audio(self):
        try:
            TTSHandler.stop()
        except Exception as e:
            print(e)
    def resume_audio(self):
        try:
            TTSHandler.resume()
        except Exception as e:
            print(e)

    def __generate_thread(self):
        TTSHandler.set_text(self.ids.text_input.text)
        TTSHandler.generate()
        self.popup.dismiss()
        Clock.unschedule(self.refresh_event)
        self.audio_generated = True
        self.__unlock_buttons()

    def __unlock_buttons(self):
        self.ids.stop.disabled = False
        self.ids.resume.disabled = False
        self.ids.save.disabled = False
        self.ids.generate_play.text = t('play')
        self.ids.generate_play.background_color = (0.5, 0.7, 1, 1)

    def __popup_refresher(self):
        self.popup.set_text(Label(text=t('generating') + (self.refresh_tick * '.')))
        self.refresh_tick += 1
        if self.refresh_tick > 3:
            self.refresh_tick = 0


class ProfilesDropDown(Spinner):
    profiles = ListProperty([])

    def __init__(self, **kwargs):
        super(ProfilesDropDown, self).__init__(**kwargs)
        self.text = t('select_profile')
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
            with open("Assets/settings.json", "r") as f:
                profiles = json.load(f)['profiles']
                for profile in profiles:
                    if profile["ModelType"] == TTSHandler.get_model_type():
                        self.profiles.append(profile["ProfileName"])
        except FileNotFoundError as e:
            print(e)
