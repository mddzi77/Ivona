from kivy.metrics import dp
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import os
class FileChooserPopup(Popup):
    def __init__(self, callback, **kwargs):
        super(FileChooserPopup, self).__init__(**kwargs)
        self.filechooser = None
        self.callback = callback
        self.title = 'Select Directory'
        self.size_hint = (0.9, 0.9)
        self.content = self.create_content()

    def create_content(self):
        layout = BoxLayout(orientation='vertical')
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        if not os.path.exists(desktop_path):
            os.makedirs(desktop_path)
        self.filechooser = FileChooserListView(path=desktop_path, dirselect=True)
        layout.add_widget(self.filechooser)

        buttons_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60), spacing=dp(10))
        buttons_layout.bind(minimum_width=buttons_layout.setter('width'))

        left_space = BoxLayout(size_hint=(0.4, None), height=dp(50))
        buttons_layout.add_widget(left_space)
        select_button = Button(
            text='Select',
            size_hint=(None, None),
            size=(dp(100), dp(50)),
            pos_hint={'center_x': 0.5},
            background_color=(0.5, 0.7, 1, 1),
            color=(1, 1, 1, 1),
            font_size=dp(18),
        )
        select_button.bind(on_press=self.on_select)
        buttons_layout.add_widget(select_button)

        cancel_button = Button(
            text='Cancel',
            size_hint=(None, None),
            size=(dp(100), dp(50)),
            pos_hint={'center_x': 0.5},
            background_color=(0.5, 0.7, 1, 1),
            color=(1, 1, 1, 1),
            font_size=dp(18),
        )
        cancel_button.bind(on_press=self.dismiss)
        buttons_layout.add_widget(cancel_button)
        layout.add_widget(buttons_layout)
        return layout

    def on_select(self, instance):
        selected_path = self.filechooser.path
        self.callback(selected_path)
        self.dismiss()
