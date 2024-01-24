from Screens.MainScreen.MainScreen import MainScreen
from Screens.NewProfileScreen.NewProfileScreen import NewProfileGridLayout
from Screens.ProfileScreen.ProfileScreen import ProfileGridLayout
from kivy.lang import Builder
from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager
import json

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'Width', '800')
Config.set('graphics', 'height', '600')

# new_data = {
#     "ProfileName": "profile_name",
#     "Path": "wav_path"
# }
#
# try:
#     with open("Screens/NewProfileScreen/profiles.json", "r") as f:
#         existing_data = json.load(f)
# except FileNotFoundError:
#     existing_data = []
#
# existing_data.append(new_data)
#
# with open("Screens/NewProfileScreen/profiles.json", "w") as f:
#     json.dump(existing_data, f, indent=2)

# print(existing_data.items())



class WindowManager(ScreenManager):
    pass


class MyApp(App):
    icon = 'custom-kivy-icon.png'
    title = 'Basic Application'

    def build(self):
        root = WindowManager()
        root.add_widget(MainScreen(name='-main_screen-'))
        root.current = '-main_screen-'  # set the current screen to main screen, just in case
        root.add_widget(NewProfileGridLayout(name='-new_profile_screen-'))
        root.add_widget(ProfileGridLayout(name='-profile_screen-'))

        return root

    # def


if __name__ == "__main__":
    MyApp().run()
