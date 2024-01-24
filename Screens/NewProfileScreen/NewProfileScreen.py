from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import json

Builder.load_file('Screens/NewProfileScreen/NewProfileScreenLayout.kv')


class NewProfileGridLayout(Screen):
    def __init__(self, **kwargs):
        super(NewProfileGridLayout, self).__init__(**kwargs)

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
