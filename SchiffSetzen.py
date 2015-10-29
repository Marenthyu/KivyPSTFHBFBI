__author__ = 'Bene'
from kivy.app import App
from kivy.uix.button import ButtonBehavior
import LayoutGame_decXdec


class SchiffSetzen(App):
    def schiffsetzen(self):
        sc = 10

        while sc > 0:
            sc= sc-1
            LayoutGame_decXdec.Pitch()
            LayoutGame_decXdec.Pitch.Wsr1(on_press=)

        pass



if __name__ == '__main__':
    SchiffSetzen().run()