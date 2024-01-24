from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

Builder.load_file('Screens/NewProfileScreen/NewProfileScreenLayout.kv')
# Window.size = (300, 500)


class NewProfileGridLayout(Screen):
    def __init__(self, **kwargs):
        super(NewProfileGridLayout, self).__init__(**kwargs)


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

    def pass_to_json(self, profile_name, file_name):

        new_data = {
            "ProfileName": profile_name,
            "Path": "Assets/" + file_name + ".wav",
            "VoiceID": None
        }

        try:
            with open("Assets/profiles.json", "r") as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            existing_data = []

        existing_data.append(new_data)

        with open("Assets/profiles.json", "w") as f:
            json.dump(existing_data, f, indent=2)
