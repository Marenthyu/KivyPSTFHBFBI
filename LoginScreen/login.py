__author__ = 'Lion'

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

Builder.load_string("""
<LoginScreen>
    f_username: username
    f_password: password
    GridLayout:
        size:120,40
        rows:3
        cols:2
        padding:5
        spacing:5
        Label:
            text: 'Benutzername:'
        TextInput:
            id: username
            multiline: False
            write_tab: False
        Label:
            text: 'Passwort:'
        TextInput:
            id: password
            password: True
            multiline: False
            write_tab: False
        Button:
            text: 'Registrieren..'
            on_press: root.manager.current = 'register'
        Button:
            text: 'Login'

<RegisterScreen>
    f_username: username
    f_password: password
    f_passwordcheck: passwordcheck
    GridLayout:
        rows: 4
        cols: 2
        padding: 5
        spacing: 5
        Label:
            text: 'Waehlen Sie ihren Benutzernamen:'
        TextInput:
            id: username
            multiline: False
            write_tab: False
        Label:
            text: 'Waehlen Sie ihr Passwort:'
        TextInput:
            id: password
            password: True
            multiline: False
            write_tab: False
        Label:
            text: 'Passwort erneut eingeben:'
        TextInput:
            id: passwordcheck
            password: True
            multiline: False
            write_tab: False
        Button:
            text: 'Login..'
            on_press: root.manager.current = 'login'
        Button:
            text: 'Registrieren'
""")

class LoginScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(RegisterScreen(name='register'))

class LoginApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    LoginApp().run()
