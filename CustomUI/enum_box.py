from enum import EnumMeta

from kivy.event import EventDispatcher
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from Localization.localization import t


class EnumBox(BoxLayout):

    def __init__(self, enum: EnumMeta, active_value, title: Label, **kwargs):
        super(EnumBox, self).__init__(**kwargs)
        self.register_event_type('on_button_selected')
        self.spacing = 10
        self.orientation = 'vertical'
        self.enum: EnumMeta = enum
        self.add_widget(title)
        self.active_value = active_value
        self.buttons = []

        for enum_val in self.enum:
            button = EnumButton(enum_val)
            self.buttons.append(button)
            button.bind(on_activate=self.on_button_release)
            self.add_widget(button)
            if enum_val.value == self.active_value:
                button.activate()

    def on_button_selected(self, enum_value):
        pass

    def on_button_release(self, x, enum_value):
        self.dispatch('on_button_selected', enum_value)
        for button in self.buttons:
            if button.enum_value.value != enum_value.value:
                button.deactivate()
            else:
                button.activate()


class EnumButton(Button):
    def __init__(self, enum_value, **kwargs):
        super(EnumButton, self).__init__(**kwargs)
        self.register_event_type('on_activate')
        self.text = t(enum_value.value)
        self.background_color = (1, 1, 1, 0.3)
        self.pos_hint = {'center_x': .5}
        self.size_hint_x = .5
        self.enum_value = enum_value
        self.selected: bool = False

    def deactivate(self):
        self.selected = False
        self.background_color = (1, 1, 1, 0.3)

    def activate(self):
        self.selected = True
        self.background_color = (1, 1, 1, 1)

    def on_release(self):
        self.dispatch('on_activate', self.enum_value)

    def on_activate(self, x):
        pass
