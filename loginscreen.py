__author__ = 'Lion'
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class LogInApp(App):

    def build(self):
        layout = GridLayout(cols=2, row_force_default=True, row_default_height=30, pos_hint={'center_x':.5, 'center_y':.5}, size_hint=(None, None))
        layout.bind(minimum_size = layout.setter('size'))
        layout.bind(height = layout.setter('top'))
        layout.add_widget(Label(text="Benutzername:", size_hint_x=None, width=120))
        layout.add_widget(TextInput(id = "name_input", size_hint_x=None, width=200, multiline=False))
        layout.add_widget(Label(text="Kennwort:", size_hint_x=None, width=120))
        layout.add_widget(TextInput(id= "pass_input", size_hint_x=None, width=200, password=True, multiline=False))
        layout.add_widget(Button(text="Registrieren"))
        return layout

if __name__ == '__main__':
        LogInApp().run()
