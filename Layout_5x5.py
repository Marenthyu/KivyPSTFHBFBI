__author__ = 'Bene'

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
import random

class Test():
    array = []

class Pitch(App):
    #  init variable to limit tries
    count = 0
    def build(self):
        
        #  init. of gridlayout in maxed square size
        h = Window.height
        w = Window.width
        global layout

        if h < w:
                    s = h
                    layout = GridLayout(cols=6, rows=6)
                    GridLayout.height = s
                    GridLayout.width = s

        else:
                    s = w
                    layout = GridLayout(cols=6, rows=6)
                    GridLayout.height = s
                    GridLayout.width = s
        
        #  declaration of two-dimensional list
        global wsr
        wsr = [[Button() for x in range(6)] for y in range(6)]

        # init. position 0,0
        wsr[0][0] = Image(source='Weiss.png')

        #  init. numbers (first row)
        for i in range (1,6):
            wsr[0][i] = Button(background_normal='Numbers/' + str(i) + '.jpg', background_down='Numbers/' + str(i) + 'C.jpg')

        # init. letters (first col)
        for j in range(1,6):
            wsr[j][0] = Button(background_normal='Letters/' + str(j) + '.jpg', background_down='Letters/' + str(j) + 'C.jpg')

        #  init. water-buttons
        for k in range (1,6):
            for l in range (1,6):
                wsr[l][k] = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', on_release=self.shootnormal)

        for i in range (1, 5):
            r = random.randint(1, 5)
            s = random.randint(1, 5)
            wsr[r][s] = Button(background_normal='Wasser.jpg', background_down='Wasser.jpg', on_release=self.shootonship)

        #  call of def "print the array"
        self.printarray(layout)

        return layout

    def printarray(self, layout):

        #  adds elements of array to layout as widget
        for m in range (0,6):
            for n in range (0,6):
                layout.add_widget(wsr[m][n])

    #  def fired when user releases button without a ship
    def  shootnormal(self,ev):
        self.count += 1
        if self.count < 6:
            print(ev)
            ev.background_normal = 'Schiff.jpg'
        else:
                print("Game Over")

    #  def fired when user releases button with ship on it
    def shootonship(self,ev):

        self.count += 1
        if self.count < 6:
            print(ev)
            ev.background_normal = 'Weiss.jpg'

            #  Call of popup "Won"

            for x in wsr:
                for y in x:
                    y.background_normal = "Weiss.jpg"

            #  self.lost()



    #  def fired when user has won the round
    def won(self):
        print('won')
        popup = Popup(title="Won!", content=Label(text="Congratulations! \n You have won the game."))
        popup.open()

    def lost(self):

        popup2 = Popup(title="Lost!", content=Label(text="You have not hit a ship. \n You have lost. Try again."), size_hint=(0.8,0.2))
        popup2.open()
if __name__ == '__main__':

    Pitch().run()