__author__ = 'Bene'
from kivy.app import App
import LayoutGame_decXdec

class Main(App):
    def build(self):
        player = LayoutGame_decXdec.Pitch().run()




if __name__ == '__main__':
    Main().run()