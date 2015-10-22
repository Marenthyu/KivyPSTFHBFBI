__author__ = 'Lion'

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from os.path import expanduser
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import os

Builder.load_file('login.kv')

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

    def existiert(self, f):
        d = os.path.dirname(f)
        if not os.path.exists(d):
            os.makedirs(d)

    def save(self, username, password):
        home = expanduser("~")
        uname = open(home + '\\schiffe\\username.txt', 'w')
        uname.write(username)
        uname.close()
        pword = open(home + '\\schiffe\\password.txt', 'w')
        pword.write(password)
        pword.close()

    def checklogin(self, username, password):
        if username == '':
            popup = Popup(title="Message",
                        content=Label(text="Bitte geben sie einen Benutzernamen ein!"),
                        size_hint=(0.8,0.2))
            popup.open()
        home = expanduser("~")
        try:
            ucheck = open(home + '\\schiffe\\username.txt', 'r')
            existingusername = ucheck.read()
            ucheck.close()
        except FileNotFoundError:
            print('File not found, making file')
            self.existiert(home + '\\schiffe\\')
            ucheck = open(home+'\\schiffe\\username.txt', 'w')
            ucheck.write('')
            existingusername = ''
            ucheck.close()
        ucheck = open(home + '\\schiffe\\username.txt', 'r')
        a = username
        b = ucheck.read()
        try:
            pcheck = open(home + '\\schiffe\\password.txt', 'r')
            password = pcheck.read()
        except FileNotFoundError:
            print('File not found, making file')
            self.existiert(home + '\\schiffe\\')
            pcheck = open(home+'\\schiffe\\password.txt', 'w')
            pcheck.write('')
            password = ''
            pcheck.close()
        pcheck = open(home + '\\schiffe\\password.txt', 'r')
        c = password
        d = pcheck.read()
        if a == b and c == d:
            popup = Popup(title = 'Message',
                conent=Label(text='Erfolreich eingeloggt!'),
                size_hint=(0.8, 0.2))
            popup.open()
        else:
            popup = Popup(title = 'Message',
                conent=Label(text='Falsches Passwort oder falscher Benutzername!'),
                size_hint=(0.8, 0.2))
            popup.open()
        ucheck.close()
        pcheck.close()

    def checkregister(self, username, password1, password2):
        home = expanduser("~")
        try:
            ucheck = open(home + '\\schiffe\\username.txt', 'r')
            existingusername = ucheck.read()
        except FileNotFoundError:
            print('File not found, making file')
            self.existiert(home + '\\schiffe\\')
            ucheck = open(home+'\\schiffe\\username.txt', 'w')
            ucheck.write('')
            existingusername = ''
        if existingusername == username.text: # Benutzername doppelt?
            popup = Popup(title="Message",
                content=Label(text="Ihr Benutzername ist leider schon vergeben!"),
                size_hint=(0.8,0.2))
            popup.open()
        else:
            if username.text in password1.text:
                popup = Popup(title="Message",
                    content=Label(text="Ihr Benutzername darf nicht Ihr Passwort sein!"),
                    size_hint=(0.8,0.2))
                popup.open()
            else:
                if password1.text != password2.text:
                    popup = Popup(title="Message",
                        content=Label(text="Ihre beiden eingegebenen Passwoerter stimmen nicht ueberein!"),
                        size_hint=(0.8,0.2))
                    popup.open()
                else:
                    if username.text in password1.text:
                        popup = Popup(title="Message",
                            content=Label(text="Ihr Passwort darf Ihren Benutzernamen nicht enthalten!"),
                            size_hint=(0.8,0.2))
                        popup.open()
                    else:
                        self.save(username.text, password1.text)
                        popup = Popup(title="Message",
                            content=Label(text="Erfolgreich registriert!"),
                            size_hint=(0.8,0.2))
                        popup.open()
                        sm.remove_widget(RegisterScreen())
                        sm.add_widget(RegisterScreen(name='register'))
                        sm.switch_to(LoginScreen(), direction='right')
        ucheck.close()

if __name__ == '__main__':
    LoginApp().run()
