__author__ = 'Lion'

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import StringProperty
from os.path import expanduser
import os
from sqlalchemy import *

Builder.load_file('bin/login.kv')

class LoginScreen(Screen):
    cinputtext = StringProperty()
    try:
        home = expanduser('~')
        uname = open(home + '\\schiffe\\username.txt', 'r')
        inputtext = uname.read()
        cinputtext = str(inputtext)
        uname.close()
    except:
        print('Gibt keinen vorhandenen Username.')
        cinputtext = ''
    pass
class RegisterScreen(Screen):
    pass
class MainScreen(Screen):
    pass
class StatistikScreen(Screen):
    cgespielteSpiele = StringProperty()
    cgewonneneSpiele = StringProperty()
    czerstoerteSchiffe = StringProperty()

    def loadTableUsers(self):
        try:
            print('load1')
            engine = create_engine('mysql+mysqlconnector://PSTSQLUser:KivyIstC00l@marenthyu.de/SchiffeVersenkenFBI')
            print('load2')
            engine.echo = True
            print('load3')
            metadata = MetaData()
            print('load4')
            metadata.create_all(engine)
            print('load5')
            metadata.bind = engine
            print('load6')
            self.users = Table('User', metadata, autoload=True)
            print('load7')
        except:
            popup6 = Popup(title="Message",
                           content=Label(text="Bitte stellen sie eine Internetverbindung her!"),
                           size_hint=(0.8, 0.4))
            popup6.open()

    def statistikenLaden(self):
        self.loadTableUsers()
        users = self.users
        stmt = users.select(users.c.Name == benutzername)
        rs = stmt.execute()
        for row in rs:
            gespielteSpiele = row.Gespielte
            self.cgespielteSpiele = str(gespielteSpiele)
            print(self.cgespielteSpiele)
            gewonneneSpiele = row.Gewonnen
            self.cgewonneneSpiele = str(gewonneneSpiele)
            print(self.cgewonneneSpiele)
            zerstoerteSchiffe = row.SchlachtschiffeZ
            self.czerstoerteSchiffe = str(zerstoerteSchiffe)
            print(self.czerstoerteSchiffe)
    pass


sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(RegisterScreen(name='register'))
sm.add_widget(MainScreen(name='main'))
sm.add_widget(StatistikScreen(name='statistiken'))


class LoginApp(App):
    benutzername = ''
    users = None

    def build(self):
        return sm


    def loadTableUsers(self):
        try:
            print('load1')
            engine = create_engine('mysql+mysqlconnector://PSTSQLUser:KivyIstC00l@marenthyu.de/SchiffeVersenkenFBI')
            print('load2')
            engine.echo = True
            print('load3')
            metadata = MetaData()
            print('load4')
            metadata.create_all(engine)
            print('load5')
            metadata.bind = engine
            print('load6')
            self.users = Table('User', metadata, autoload=True)
            print('load7')
        except:
            popup6 = Popup(title="Message",
                           content=Label(text="Bitte stellen sie eine Internetverbindung her!"),
                           size_hint=(0.8, 0.4))
            popup6.open()


    def existiert(self, f):
        d = os.path.dirname(f)
        if not os.path.exists(d):
            os.makedirs(d)


    def save(self, username, password):
        cusername = str(username)
        cpassword = str(password)
        self.loadTableUsers()
        users = self.users
        if users is not None:
            engine = create_engine('mysql+mysqlconnector://PSTSQLUser:KivyIstC00l@marenthyu.de/SchiffeVersenkenFBI')
            engine.echo = True
            metadata = MetaData()
            metadata.create_all(engine)
            metadata.bind = engine
            ins = users.insert().values(Name=cusername, Passwort=cpassword)
            str(ins)
            conn = engine.connect()
            result = conn.execute(ins)
            conn.close()


    def yolo(self, loginbutton, popup1):
        loginbutton.disabled = True
        loginbutton.background_color = [0.7, 0.7, 0.7, 1]
        loginbutton.canvas.ask_update()
        popup1.open()
        popup1.canvas.clear()
        popup1.canvas.draw()


    def checklogin(self, username, password, loginbutton, savebenutzername):
        print(savebenutzername.active)
        popup0 = Popup(title="Message",
                       content=Label(text="Bitte geben sie einen Benutzernamen ein!"),
                       size_hint=(0.8, 0.4))
        popup1 = Popup(title="Message",
                       content=Label(text="Loggin in..."),
                       size_hint=(0.8, 0.4))
        popup2 = Popup(title="Message",
                       content=Label(text="Falscher Benutzername oder Passwort!"),
                       size_hint=(0.8, 0.4))
        popup3 = Popup(title="Message",
                       content=Label(text="Erfolgreich eingeloggt!"),
                       size_hint=(0.8, 0.4))

        self.yolo(loginbutton, popup1)

        if username == '':
            popup0.open()
            popup1.dismiss()
            loginbutton.background_color = [1, 1, 1, 1]
            loginbutton.disabled = False
            return
        cusername = str(username)
        cpasswort = str(password)
        self.loadTableUsers()
        users = self.users
        if users is not None:
            stmt = users.select(and_(users.c.Name == cusername, users.c.Passwort == cpasswort))
            rs = stmt.execute()
            i = 0
            for row in rs:
                i = i + 1
            if i == 1:
                if savebenutzername.active:
                    try:
                        home = expanduser("~")
                        uname = open(home + '\\schiffe\\username.txt', 'w')
                        uname.write(username)
                        print('Username.txt wurde erfolgreich beschrieben!')
                        uname.close()
                    except:
                        try:
                            home = expanduser("~")
                            print('File not found, making file')
                            self.existiert(home + '\\schiffe\\')
                            ucheck = open(home+'\\schiffe\\username.txt', 'w')
                            ucheck.write(username)
                            ucheck.close()
                        except:
                            print('Couldnt read or write.....')
                else:
                    try:
                        home = expanduser("~")
                        os.remove(home + '\\schiffe\\username.txt')
                        print('Deleting username.txt completetd!')
                    except:
                        print('Datei nicht vorhanden!')

                global benutzername
                benutzername = cusername
                popup3.open()
                popup1.dismiss()
                sm.remove_widget(LoginScreen())
                sm.add_widget(LoginScreen(name="login"))
                sm.switch_to(MainScreen(), direction='up')
            else:
                popup2.open()
                popup1.dismiss()
        loginbutton.disabled = False
        loginbutton.background_color = [1, 1, 1, 1]
        popup1.dismiss()


    def checkregister(self, username, password1, password2):
        self.loadTableUsers()
        users = self.users
        if users is not None:
            cusername = str(username.text)
            stmt = users.select(users.c.Name == cusername)
            rs = stmt.execute()
            i = 0
            for row in rs:
                i = i + 1
            if i >= 1:
                popup7 = Popup(title="Message",
                               content=Label(text="Ihr Benutzername ist leider schon vergeben!"),
                               size_hint=(0.8, 0.4))
                popup7.open()
            else:
                if username.text in password1.text:
                    popup8 = Popup(title="Message",
                                   content=Label(text="Ihr Benutzername darf nicht Ihr Passwort sein!"),
                                   size_hint=(0.8, 0.4))
                    popup8.open()
                else:
                    if password1.text != password2.text:
                        popup9 = Popup(title="Message",
                                       content=Label(
                                           text="Ihre beiden eingegebenen Passwoerter stimmen nicht ueberein!"),
                                       size_hint=(0.8, 0.4))
                        popup9.open()
                    else:
                        if username.text in password1.text:
                            popup10 = Popup(title="Message",
                                            content=Label(
                                                text="Ihr Passwort darf Ihren Benutzernamen nicht enthalten!"),
                                            size_hint=(0.8, 0.4))
                            popup10.open()
                        else:
                            self.save(username.text, password1.text)
                            popup11 = Popup(title="Message",
                                            content=Label(text="Erfolgreich registriert!"),
                                            size_hint=(0.8, 0.4))
                            popup11.open()
                            sm.remove_widget(RegisterScreen())
                            sm.add_widget(RegisterScreen(name='register'))
                            sm.switch_to(LoginScreen(), direction='right')

    def logout(self):
        global benutzername
        benutzername = ''
        sm.remove_widget(LoginScreen())
        sm.add_widget(LoginScreen())
        sm.switch_to(LoginScreen(), direction='left')



if __name__ == '__main__':
    LoginApp().run()
