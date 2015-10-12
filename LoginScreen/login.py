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
            on_press: app.checklogin(username.text, password.text)

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
            on_press: root.manager.current = 'successregister'

<LoggedInScreen>
    BoxLayout:
        orientation: 'vertical'
        pos_hint: { 'center_x' : .5, 'center_y' : .5 }
        size_hint: None, None
        Label:
            text: 'Sie haben sich erfolgreich eingeloggt!'
        Button:
            text: 'Ok!'
            on_press: root.manager.current = 'menu'

<SuccessRegisterScreen>
    BoxLayout:
        orientation: 'vertical'
        pos_hint: { 'center_x' : .5, 'center_y' : .5 }
        size_hint: None, None
        Label:
            text: 'Sie haben sich erfolgreich registriert!'
        Button:
            text: 'Ok!'
            on_press: root.manager.current = 'login'

<UnSuccesLogin>
    BoxLayout:
        orientation: 'vertical'
        pos_hint: { 'center_x': .5, 'center_y': .5 }
        size_hint: None, None
        Label:
            text: 'Ihr Passwort oder ihr Benutzername war falsch, bitte registrieren sie sich!'
        Button:
            text: 'Ok!'
            on_press: root.manager.current = 'register'

""")

class LoginScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

class LoggedInScreen(Screen):
    pass

class SuccessRegisterScreen(Screen):
    pass

class UnSuccesLogin(Screen):
    pass

sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(RegisterScreen(name='register'))
sm.add_widget(LoggedInScreen(name='loggedin'))
sm.add_widget(SuccessRegisterScreen(name='successregister'))
sm.add_widget(UnSuccesLogin(name='unsuccesslogin'))



class LoginApp(App):
    def build(self):
        return sm

    def save(self, username, password):
        uname = open('C:/Users/Public/Documents/username.txt','w')
        uname.write(username)
        uname.close()
        pword = open('C:/Users/Public/Documents/password.txt', 'w')
        pword.write(password)
        pword.close()

    def checklogin(self, username, password):
        ucheck = open('C:/Users/Public/Documents/username.txt', 'r')
        a = username
        b = ucheck.read()
        pcheck = open('C:/Users/Public/Documents/password.txt', 'r')
        c = password
        d = pcheck.read()
        if a == b and c == d:
            sm.switch_to(LoggedInScreen())
        else:
            sm.switch_to(UnSuccesLogin())


if __name__ == '__main__':
    LoginApp().run()
