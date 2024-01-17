from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file('Screens/ProfileScreen/ProfileScreenLayout.kv')


class ProfileGridLayout(Screen):

    def __init__(self, **kwargs):
        super(ProfileGridLayout, self).__init__(**kwargs)
