from kivy.app import App
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

from CustomUI.enum_box import EnumBox
from Localization.localization import t, Localization, Language
from TextToSpeech.tts_handler import ModelType, TTSHandler

Builder.load_file('Screens/SettingsScreen/SettingsScreen.kv')


class SettingsScreen(Screen):

    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.__add_language_box()
        self.__add_model_box()
        self.new_language = None
        self.new_model = None

    def apply_settings(self):
        if self.new_model is not None and self.new_model != TTSHandler.get_model_type():
            TTSHandler.set_model(self.new_model)
        if self.new_language is not None and self.new_language != Localization().get_language():
            Localization().set_language(self.new_language)
            App.get_running_app().on_language_change()
            return
        self.manager.transition.direction = 'left'
        self.manager.current = '-main_screen-'

    def __add_language_box(self):
        language_label = Label(text=t('language'))
        language_box = EnumBox(Language, Localization().get_language(), language_label)
        language_box.bind(on_button_selected=lambda x, v: self.__set_language_temporarily(v))
        self.ids.options.add_widget(language_box)

    def __add_model_box(self):
        model_label = Label(text=t('model'))
        model_box = EnumBox(ModelType, TTSHandler.get_model_type(), model_label)
        model_box.bind(on_button_selected=lambda x, v: self.__set_model_temporarily(v))
        self.ids.options.add_widget(model_box)

    def __set_language_temporarily(self, language):
        self.new_language = language

    def __set_model_temporarily(self, model):
        self.new_model = model
