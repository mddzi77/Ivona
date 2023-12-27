from MainScreen.MainScreen import MyGridLayout
from kivy.app import App
from kivy.config import Config

Config.set('graphics', 'Width', '800')
Config.set('graphics', 'height', '600')



class MyApp(App):
    icon = 'custom-kivy-icon.png'
    title = 'Basic Application'

    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()
