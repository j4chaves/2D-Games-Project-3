__author__ = 'Jacob'

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from Game import Game

class MainMenu(BoxLayout):
    header = Label(text='[size=36]Jacob Chaves \n   Project 3[/size]', size_hint=(.5, .25), pos_hint={'center_x': .5}, markup=True)
    level1 = Button(text='Level 1', size_hint=(.5, .25), pos_hint = {'center_x': .5})
    level2 = Button(text='Level 2', size_hint=(.5, .25), pos_hint = {'center_x': .5})

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.orientation = 'vertical'

    def createMenu(self):
        self.add_widget(self.header)
        self.add_widget(self.level1)
        self.add_widget(self.level2)

    def update(self, dt):
        pass

    def on_touch_down(self, touch):
        if self.level1.collide_point(touch.x, touch.y):
           pass# game = Game()
        elif self.level2.collide_point(touch.x, touch.y):
            pass