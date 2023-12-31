from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.core.window import Window
import fitz  # to jest jak cos biblio PyMuPDF, niestety zainstalowac trza, ale czyta duzo wiecej niz pdf

textinput = TextInput(multiline=True)  # imo lepiej zeby to globalne, bo pozniej do algorytmu zeby zczytal czy cos


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 2

        # Elements
        labelName = Label(text='Ivona', font_size=35)
        buttonNewProfile = Button(text='New Profile', size_hint_y=None, height=50)
        buttonProfile = Button(text='Profile', size_hint_y=None, height=50)
        buttonExit = Button(text='Exit', size_hint_y=None, height=50)
        # BoxLayout for Buttons - LEFT
        button_layout = BoxLayout(orientation='vertical', spacing=90, padding=15, size_hint_x=None, width=350)
        button_layout.add_widget(labelName)
        button_layout.add_widget(buttonNewProfile)
        button_layout.add_widget(buttonProfile)
        button_layout.add_widget(buttonExit)

        # BoxLayout for Text Panel - RIGHT
        text_layout = BoxLayout(orientation='vertical', spacing=15, padding=15)
        self.text_input = textinput
        text_layout.add_widget(self.text_input)

        # Add BoxLayouts to the GridLayout
        self.add_widget(button_layout)
        self.add_widget(text_layout)

        # Drop Handler
        Window.bind(on_dropfile=self.handle_dropfile)

    def handle_dropfile(self, window, file_path):       #nwm czemu w dokumenacji bardzo chca tego windowa dalej, ale inaczej nie dziala, to niech ma
        if self.text_input.collide_point(*Window.mouse_pos):
            self.load_pdf(file_path)

    @staticmethod       #Pycharm mi tak powiedzial, ze git, no to chyba git :skull:
    def load_pdf(file_path):
        try:
            byte_string = file_path
            proper_path = byte_string.decode('utf-8')
            doc = fitz.open(proper_path)
            pdf_text = ""
            for page_num in range(doc.page_count):
                page = doc[page_num]
                pdf_text += page.get_text()

            textinput.text = pdf_text
        except Exception as e:
            popup = Popup(title='ERROR', content=Label(text=f"Error:{str(e)}"), size_hint=(None, None), size=(400, 200))
            popup.open()
