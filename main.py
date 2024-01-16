from Screens.MainScreen.MainScreen import MainScreen
from Screens.NewProfileScreen.NewProfileScreen import NewProfileGridLayout
from Screens.ProfileScreen.ProfileScreen import ProfileGridLayout
from kivy.lang import Builder
from kivy.app import App
from kivy.config import Config

Builder.load_file('Screens/MainScreen/MainScreenLayout.kv')
Builder.load_file('Screens/ProfileScreen/ProfileScreenLayout.kv')
Builder.load_file('Screens/NewProfileScreen/NewProfileScreenLayout.kv')

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'Width', '800')
Config.set('graphics', 'height', '600')


class MyApp(App):
    icon = 'custom-kivy-icon.png'
    title = 'Basic Application'

    def build(self):
        return MainScreen()

    # def show(self, widget):



if __name__ == "__main__":
    MyApp().run()
