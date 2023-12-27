from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView
class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 2
        # Elements
        labelName = Label(text='Ivona',font_size=35)
        buttonNewProfile = Button(text='New Profile',size_hint_y=None, height=50)
        buttonProfile = Button(text='Profile',size_hint_y=None, height=50)
        buttonExit = Button(text='Exit', size_hint_y=None, height=50)
        # BoxLayout for Buttons - LEFT
        button_layout = BoxLayout(orientation='vertical',spacing=90,padding=15, size_hint_x=None,width=350)
        button_layout.add_widget(labelName)
        button_layout.add_widget(buttonNewProfile)
        button_layout.add_widget(buttonProfile)
        button_layout.add_widget(buttonExit)

        # BoxLayout for Text Panel - RIGHT
        text_layout = BoxLayout(orientation='vertical', spacing=15, padding=15)
        self.text_input = TextInput(multiline=True)
        text_layout.add_widget(self.text_input)

        # Drop Load File
        file_chooser = FileChooserListView( height=100) #ten file chooser to do wyjebania, cos innego
        file_chooser.bind(on_dropfile=self.on_file_drop)

        # Add Widgets to the Grid
        self.add_widget(button_layout)
        self.add_widget(text_layout)
        #self.add_widget(file_chooser) jakis inny widget na drop file to load (?)

    def on_file_drop(self, filepath):
        # Handling Dropped File                         //Wez tu wjeb te walki z pdf itd. najlepiej w osobnym pliku .py zeby nie nasrac tu
        print(f'Dropped file boys: {filepath}')