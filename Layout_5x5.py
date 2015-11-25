__author__ = 'Bene'

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.button import Button
import time
import random


class Pitch(App):
    count = 0
    def build(self):

        #  Initialisiert Gridlayout in maximaler quadtratischer Groesse
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

        #  Deklariert zweidimensionale Liste
        global wsr
        wsr = [[Button() for x in range(6)] for y in range(6)]

        # init. Platz 0,0
        wsr[0][0] = Image(source='Weiss.png')

        #  init. Zahlen (erste Reihe)
        for i in range (1,6):
            wsr[0][i] = Button(background_normal='Numbers/' + str(i) + '.jpg', background_down='Numbers/' + str(i) + 'C.jpg')

        # init. Buchstaben (erste Spalte)
        for j in range(1,6):
            wsr[j][0] = Button(background_normal='Letters/' + str(j) + '.jpg', background_down='Letters/' + str(j) + 'C.jpg')

        #  init. Wasserfelder
        for k in range (1,6):
            for l in range (1,6):
                wsr[l][k] = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', on_release=self.shootnormal)

        for i in range (1, 5):
            r = random.randint(1, 5)
            s = random.randint(1, 5)
            wsr[r][s] = Button(background_normal='Wasser.jpg', background_down='Wasser.jpg', on_release=self.shootonship)


        #  Aufruf def "print des Arrays"
        self.printarray(layout)



        return layout

    def printarray(self, layout):

        #  print der Liste
        for m in range (0,6):
            for n in range (0,6):
                layout.add_widget(wsr[m][n])

    def  shootnormal(self,ev):

        self.count += 1
        if self.count < 5:
            print(ev)
            ev.background_normal = 'Schiff.jpg'

        else:
            print("Game Over")

    def shootonship(self,ev):

        self.count += 1
        if self.count < 5:
            print(ev)
            ev.background_normal = 'Weiss.jpg'

        else:
            print("Game Over")








if __name__ == '__main__':

    Pitch().run()