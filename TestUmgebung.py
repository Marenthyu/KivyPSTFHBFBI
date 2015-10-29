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
                            layout = GridLayout(cols=2, rows=2)
                            GridLayout.height = s
                            GridLayout.width = s

                else:
                            s = w
                            layout = GridLayout(cols=2, rows=2)
                            GridLayout.height = s
                            GridLayout.width = s

                layout.add_widget(Image(source='Weiss.png'))
                layout.add_widget(Button(background_normal='Numbers/1.jpg', background_down='Numbers/1C.jpg'))
                layout.add_widget(Button(background_normal='Letters/A.jpg', background_down='Letters/AC.jpg'))
                layout.add_widget(Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg'))
                return layout

if __name__ == '__main__':
    Pitch().run()