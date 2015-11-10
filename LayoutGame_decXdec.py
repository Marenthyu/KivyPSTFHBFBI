__author__ = 'Bene'

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.button import Button, ButtonBehavior


class Pitch(App):
       def build(self):

                h = Window.height
                w = Window.width

                if h < w:
                            s = h
                            layout = GridLayout(cols=11, rows=11)
                            GridLayout.height = s
                            GridLayout.width = s

                else:
                            s = w
                            layout = GridLayout(cols=11, rows=11)
                            GridLayout.height = s
                            GridLayout.width = s

                wsr = [[Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg') for x in range(11)] for y in range(11)]
                print(wsr[4][7])


                layout.add_widget(Image(source='Weiss.png'))
                for i in range (1,11):
                    wsr[0][i] =Button(background_normal='Numbers/' + str(i) + '.jpg', background_down='Numbers/' + str(i) + 'C.jpg')
                    layout.add_widget(wsr[0][i])

                for j in range(1,11):
                    wsr[j][0] =Button(background_normal='Letters/' + str(j) + '.jpg', background_down='Letters/' + str(j) + 'C.jpg')
                    layout.add_widget(Button(background_normal='Letters/' + str(j) +'.jpg', background_down='Letters/' + str(j) + 'C.jpg'))
                for k in range (1,10):
                    wsr[k][k] = Button(background_normal='Wasser.jpg', background_down='Wasser.jpg')
                    layout.add_widget(wsr[k][k])






                return layout



if __name__ == '__main__':
    Pitch().run()
