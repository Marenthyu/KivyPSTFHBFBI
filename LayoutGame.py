__author__ = 'Bene'

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class Pitch(App):

        def build(self):

                h = Window.height
                w = Window.width

                if h < w:
                            s = h
                            layout = GridLayout(cols=14, rows=16)
                            GridLayout.height = s
                            GridLayout.width = s

                else:
                            s = w
                            layout = GridLayout(cols=14, rows=16)
                            GridLayout.height = s
                            GridLayout.width = s

                Wsr1 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr2 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr3 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr4 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr5 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr6 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr7 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr8 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr9 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr10 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr11 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr12 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr13 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr14 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr15 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr16 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr17 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr18 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr19 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr20 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr21 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr22 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr23 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr24 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr25 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr26 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr27 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr28 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr29 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr30 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr31 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr32 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr33 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr34 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr35 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr36 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr37 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr38 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr39 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr40 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr41 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr42 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr43 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr44 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr45 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr46 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr47 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr48 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr49 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr50 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr51 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr52 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr53 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr54 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr55 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr56 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr57 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr58 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr59 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr60 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr61 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr62 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr63 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr64 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr65 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr66 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr67 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr68 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr69 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr70 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr71 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr72 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr73 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr74 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr75 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr76 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr77 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr78 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr79 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr80 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr81 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr82 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr83 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr84 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr85 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr86 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr87 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr88 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr89 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr90 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr91 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr92 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr93 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr94 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr95 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr96 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr97 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr98 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr99 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr100 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr101 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr102 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr103 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr104 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr105 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr106 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr107 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr108 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr109 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr110 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr111 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr112 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr113 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr114 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr115 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr116 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr117 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr118 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr119 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr120 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr121 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr122 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr123 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr124 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr125 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr126 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr127 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr128 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr129 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr130 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr131 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr132 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr133 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr134 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr135 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr136 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr137 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr138 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr139 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr140 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr141 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr142 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr143 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr144 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr145 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr146 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr147 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr148 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr149 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr150 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr151 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr152 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr153 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr154 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr155 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr156 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr157 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr158 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr159 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr160 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr161 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr162 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr163 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr164 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr165 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr166 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr167 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr168 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')
                Wsr169 = Button(background_normal='Wasser.jpg', background_down='Schiff.jpg', background_disabled_normal='Schiff.jpg')

                layout.add_widget(Image(source='Weiss.png'))
                layout.add_widget(Button(background_normal='Numbers/1.jpg', background_down='Numbers/1C.jpg'))
                layout.add_widget(Button(background_normal='Numbers/2.jpg', background_down='Numbers/2C.jpg'))
                layout.add_widget(Button(background_normal='Numbers/3.jpg', background_down='Numbers/3C.jpg'))
                layout.add_widget(Button(background_normal='Numbers/4.jpg', background_down='Numbers/4C.jpg'))
                layout.add_widget(Button(background_normal='Numbers/5.jpg', background_down='Numbers/5C.jpg'))
                layout.add_widget(Button(background_normal='Numbers/6.jpg', background_down='Numbers/6C.jpg'))
                layout.add_widget(Button(background_normal='Numbers/7.jpg', background_down='Numbers/7C.jpg'))
                layout.add_widget(Button(background_normal='Numbers/8.jpg', background_down='Numbers/8C.jpg'))
                layout.add_widget(Button(background_normal='Numbers/9.jpg', background_down='Numbers/9C.jpg'))
                layout.add_widget(Button(background_normal='Numbers/10.jpg', background_down='Numbers/10C.jpg'))
                layout.add_widget(Button(background_normal='Numbers/11.jpg', background_down='Numbers/11C.jpg'))
                layout.add_widget(Button(background_normal='Numbers/12.jpg', background_down='Numbers/12C.jpg'))
                layout.add_widget(Button(background_normal='Numbers/13.jpg', background_down='Numbers/13C.jpg'))
                layout.add_widget(Button(background_normal='Letters/A.jpg', background_down='Letters/AC.jpg'))
                layout.add_widget(Wsr1)
                layout.add_widget(Wsr2)
                layout.add_widget(Wsr3)
                layout.add_widget(Wsr4)
                layout.add_widget(Wsr5)
                layout.add_widget(Wsr6)
                layout.add_widget(Wsr7)
                layout.add_widget(Wsr8)
                layout.add_widget(Wsr9)
                layout.add_widget(Wsr10)
                layout.add_widget(Wsr11)
                layout.add_widget(Wsr12)
                layout.add_widget(Wsr13)
                layout.add_widget(Button(background_normal='Letters/B.jpg', background_down='Letters/BC.jpg'))
                layout.add_widget(Wsr14)
                layout.add_widget(Wsr15)
                layout.add_widget(Wsr16)
                layout.add_widget(Wsr17)
                layout.add_widget(Wsr18)
                layout.add_widget(Wsr19)
                layout.add_widget(Wsr20)
                layout.add_widget(Wsr21)
                layout.add_widget(Wsr22)
                layout.add_widget(Wsr23)
                layout.add_widget(Wsr24)
                layout.add_widget(Wsr25)
                layout.add_widget(Wsr26)
                layout.add_widget(Button(background_normal='Letters/C.jpg', background_down='Letters/CC.jpg'))
                layout.add_widget(Wsr27)
                layout.add_widget(Wsr28)
                layout.add_widget(Wsr29)
                layout.add_widget(Wsr30)
                layout.add_widget(Wsr31)
                layout.add_widget(Wsr32)
                layout.add_widget(Wsr33)
                layout.add_widget(Wsr34)
                layout.add_widget(Wsr35)
                layout.add_widget(Wsr36)
                layout.add_widget(Wsr37)
                layout.add_widget(Wsr38)
                layout.add_widget(Wsr39)
                layout.add_widget(Button(background_normal='Letters/D.jpg', background_down='Letters/DC.jpg'))
                layout.add_widget(Wsr40)
                layout.add_widget(Wsr41)
                layout.add_widget(Wsr42)
                layout.add_widget(Wsr43)
                layout.add_widget(Wsr44)
                layout.add_widget(Wsr45)
                layout.add_widget(Wsr46)
                layout.add_widget(Wsr47)
                layout.add_widget(Wsr48)
                layout.add_widget(Wsr49)
                layout.add_widget(Wsr50)
                layout.add_widget(Wsr51)
                layout.add_widget(Wsr52)
                layout.add_widget(Button(background_normal='Letters/E.jpg', background_down='Letters/EC.jpg'))
                layout.add_widget(Wsr53)
                layout.add_widget(Wsr54)
                layout.add_widget(Wsr55)
                layout.add_widget(Wsr56)
                layout.add_widget(Wsr57)
                layout.add_widget(Wsr58)
                layout.add_widget(Wsr59)
                layout.add_widget(Wsr60)
                layout.add_widget(Wsr61)
                layout.add_widget(Wsr62)
                layout.add_widget(Wsr63)
                layout.add_widget(Wsr64)
                layout.add_widget(Wsr65)
                layout.add_widget(Button(background_normal='Letters/F.jpg', background_down='Letters/FC.jpg'))
                layout.add_widget(Wsr66)
                layout.add_widget(Wsr67)
                layout.add_widget(Wsr68)
                layout.add_widget(Wsr69)
                layout.add_widget(Wsr70)
                layout.add_widget(Wsr71)
                layout.add_widget(Wsr72)
                layout.add_widget(Wsr73)
                layout.add_widget(Wsr74)
                layout.add_widget(Wsr75)
                layout.add_widget(Wsr76)
                layout.add_widget(Wsr77)
                layout.add_widget(Wsr78)
                layout.add_widget(Button(background_normal='Letters/G.jpg', background_down='Letters/GC.jpg'))
                layout.add_widget(Wsr79)
                layout.add_widget(Wsr80)
                layout.add_widget(Wsr81)
                layout.add_widget(Wsr82)
                layout.add_widget(Wsr83)
                layout.add_widget(Wsr84)
                layout.add_widget(Wsr85)
                layout.add_widget(Wsr86)
                layout.add_widget(Wsr87)
                layout.add_widget(Wsr88)
                layout.add_widget(Wsr89)
                layout.add_widget(Wsr90)
                layout.add_widget(Wsr91)
                layout.add_widget(Button(background_normal='Letters/H.jpg', background_down='Letters/HC.jpg'))
                layout.add_widget(Wsr92)
                layout.add_widget(Wsr93)
                layout.add_widget(Wsr94)
                layout.add_widget(Wsr95)
                layout.add_widget(Wsr96)
                layout.add_widget(Wsr97)
                layout.add_widget(Wsr98)
                layout.add_widget(Wsr99)
                layout.add_widget(Wsr100)
                layout.add_widget(Wsr101)
                layout.add_widget(Wsr102)
                layout.add_widget(Wsr103)
                layout.add_widget(Wsr104)
                layout.add_widget(Button(background_normal='Letters/I.jpg', background_down='Letters/IC.jpg'))
                layout.add_widget(Wsr105)
                layout.add_widget(Wsr106)
                layout.add_widget(Wsr107)
                layout.add_widget(Wsr108)
                layout.add_widget(Wsr109)
                layout.add_widget(Wsr110)
                layout.add_widget(Wsr111)
                layout.add_widget(Wsr112)
                layout.add_widget(Wsr113)
                layout.add_widget(Wsr114)
                layout.add_widget(Wsr115)
                layout.add_widget(Wsr116)
                layout.add_widget(Wsr117)
                layout.add_widget(Button(background_normal='Letters/J.jpg', background_down='Letters/JC.jpg'))
                layout.add_widget(Wsr118)
                layout.add_widget(Wsr119)
                layout.add_widget(Wsr120)
                layout.add_widget(Wsr121)
                layout.add_widget(Wsr122)
                layout.add_widget(Wsr123)
                layout.add_widget(Wsr124)
                layout.add_widget(Wsr125)
                layout.add_widget(Wsr126)
                layout.add_widget(Wsr127)
                layout.add_widget(Wsr128)
                layout.add_widget(Wsr129)
                layout.add_widget(Wsr130)
                layout.add_widget(Button(background_normal='Letters/K.jpg', background_down='Letters/KC.jpg'))
                layout.add_widget(Wsr131)
                layout.add_widget(Wsr132)
                layout.add_widget(Wsr133)
                layout.add_widget(Wsr134)
                layout.add_widget(Wsr135)
                layout.add_widget(Wsr136)
                layout.add_widget(Wsr137)
                layout.add_widget(Wsr138)
                layout.add_widget(Wsr139)
                layout.add_widget(Wsr140)
                layout.add_widget(Wsr141)
                layout.add_widget(Wsr142)
                layout.add_widget(Wsr143)
                layout.add_widget(Button(background_normal='Letters/L.jpg', background_down='Letters/LC.jpg'))
                layout.add_widget(Wsr144)
                layout.add_widget(Wsr145)
                layout.add_widget(Wsr146)
                layout.add_widget(Wsr147)
                layout.add_widget(Wsr148)
                layout.add_widget(Wsr149)
                layout.add_widget(Wsr150)
                layout.add_widget(Wsr151)
                layout.add_widget(Wsr152)
                layout.add_widget(Wsr153)
                layout.add_widget(Wsr154)
                layout.add_widget(Wsr155)
                layout.add_widget(Wsr156)
                layout.add_widget(Button(background_normal='Letters/M.jpg', background_down='Letters/MC.jpg'))
                layout.add_widget(Wsr157)
                layout.add_widget(Wsr158)
                layout.add_widget(Wsr159)
                layout.add_widget(Wsr160)
                layout.add_widget(Wsr161)
                layout.add_widget(Wsr162)
                layout.add_widget(Wsr163)
                layout.add_widget(Wsr164)
                layout.add_widget(Wsr165)
                layout.add_widget(Wsr166)
                layout.add_widget(Wsr167)
                layout.add_widget(Wsr168)
                layout.add_widget(Wsr169)

                return layout


if __name__ == '__main__':
    Pitch().run()
