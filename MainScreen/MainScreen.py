from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.lang import Builder
from .FileRead import handle_dropfile

Builder.load_file('MainScreen/MainScreenLayout.kv')


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        '''
        V to jakby nie bylo .kv || jakby ktos chcial sie zasugerowac, pozniej do wywalenia
        
        self.cols = 2

        # Elements
        label_name = Label(text='Ivona', font_size=35)
        button_new_profile = Button(text='New Profile', size_hint_y=None, height=50)
        button_profile = Button(text='Profile', size_hint_y=None, height=50)
        button_exit = Button(text='Exit', size_hint_y=None, height=50)
        # BoxLayout for Buttons - LEFT
        button_layout = BoxLayout(orientation='vertical', spacing=90, padding=15, size_hint_x=None, width=350)
        button_layout.add_widget(label_name)
        button_layout.add_widget(button_new_profile)
        button_layout.add_widget(button_profile)
        button_layout.add_widget(button_exit)

        # BoxLayout for Text Panel - RIGHT
        text_layout = BoxLayout(orientation='vertical', spacing=15, padding=15)
        self.text_input = textinput
        text_layout.add_widget(self.text_input)

        # Add BoxLayouts to the GridLayout
        self.add_widget(button_layout)
        self.add_widget(text_layout)
        '''

        # Drag & Drop File Handler
        Window.bind(on_dropfile=lambda window, file_path: handle_dropfile(window, file_path, self.ids.text_input))  # tu bez kivy self.text_input
        # tak samo pozniej zbieranie textu i wszystkiego z kivy przez ID
