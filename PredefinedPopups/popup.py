from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.uix.popup import Popup


class PopupBase:
    def __init__(self):
        self._popup = Popup(size_hint=(None, None), size=(300, 180), auto_dismiss=False)
        self._modal_view = ModalView(size_hint=(1, 1), background_color=(0, 0, 0, .7))
        self._modal_view.add_widget(self._popup)

    def show(self):
        self._modal_view.open()

    def dismiss(self):
        self._modal_view.dismiss()

    def set_size(self, size):
        self._popup.size = size

    def set_background_color(self, color):
        self._modal_view.background_color = color


class TextPopup(PopupBase):
    def __init__(self, text: str | Label, title: str):
        super().__init__()
        self.__text = None
        self.set_text(text)
        self._popup.title = title

    def set_text(self, text: str | Label):
        self._popup.content = Label(text=text) if type(text) is str else text


class OkPopup(PopupBase):
    def __init__(self, button_callback, button_text: str = 'Ok', title: str = None):
        super().__init__()
        self.__button = Button(text=button_text, pos_hint={'center_x': 0.5, 'center_y': .5})
        self.__button.bind(on_release=button_callback)
        self.set_size((280, 120))
        self.set_button_size(size_hint=(.2, .5))
        if title is not None:
            self._popup.title = title
        self._popup.content = self.__button

    def set_button_text(self, text):
        self.__button.text = text

    def set_button_size(self, size: tuple = None, size_hint: tuple = None):
        if size is not None:
            self.__button.size = size
        elif size_hint is not None:
            self.__button.size_hint = size_hint
        else:
            raise Exception('No size or size_hint provided')
