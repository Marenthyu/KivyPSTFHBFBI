__author__ = 'Bene'
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class Main(App):
    def build(self):
        self.won()
        self.lost()

    def won(self):
        print('won')
        popup = Popup(title="Won!", content=Label(text="Congratulations! \n You have won the game."))
        popup.open()

    def lost(self):

        popup2 = Popup(title="Lost!", content=Label(text="You have not hit a ship. \n You have lost. Try again."), size_hint=(0.8,0.2))
        popup2.open()

if __name__ == '__main__':
    Main().run()