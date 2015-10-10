__author__ = 'Lion'

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

Builder.load_string("""
<LoginScreen>
    f_username: username
    f_password: password
    GridLayout:
        size:400, 120
        size_hint: None, None
        pos_hint: { 'center_x' : .5, 'center_y' : .5 }
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
        size:470, 160
        size_hint: None, None
        pos_hint: { 'center_x' : .5, 'center_y' : .5 }
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
            on_press: app.save(username.text, password.text)
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

    def save(self, username, password):
        fob = open('C:/Users/Public/Documents/test.txt','w')
        fob.write(username + "\n")
        fob.write(password)
        fob.close()

if __name__ == '__main__':
    LoginApp().run()
