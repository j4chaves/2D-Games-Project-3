__author__ = 'Jacob Chaves'
"""
2D Game Programming
Project 3
Game Class

This is the main game file that controls the flow of the game.

GAME CLASS:
    This class controls the main game mechanics and what is happening on screen.

    VARIABLES:
        charList - list of all the Defenders on the screen
        enemyList - list of all the Enemies of the screen


    METHODS:

GAMEAPP CLASS:
    Top level class that just starts the game and the Clock for updating the screen.
"""

from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config  # needed to configure the window size
from kivy.core.window import Window, WindowBase
from kivy.graphics import Color
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.logger import Logger
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
import os
import random
from Defender import Defender
from Enemy import Enemy
from Row import Row


"""
TODO
1. Create ROWS and allow selection of ROWS
2. Create different profiles for Enemies and Defenders
3. Rewrite Game.update() method.  The logic needs to be worked out
3. Get animated images for anemies and defenders
4. Create branch with gridlayout
5. Comment the files
6. Write Documentation

BUGS

1. When placing Defenders rapidly, the whole game speeds up.  This causes an error hen an enemy needs to be removed from
   the enemyList.  The program can't seem to find the enemy.
"""


# GAME CLASS
class Game(BoxLayout):
    enemySpawnCounter = 0
    defenderList = []
    enemyList = []
    defenderSelection = 1
    header = Row()
    row1 = Row()
    row2 = Row()
    row3 = Row()
    row4 = Row()
    row5 = Row()

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(self.header)
        self.add_widget(self.row1)
        self.add_widget(self.row2)
        self.add_widget(self.row3)
        self.add_widget(self.row4)
        self.add_widget(self.row5)

        #Taken from Kivy window Documentation
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self.on_keyboard_down)

    #THIS WHOLE METHOD NEEDS TO BE THOUGHT OUT ON PAPER BEFORE BEING IMPLEMENTED
    def update(self, dt):
        pass


    def on_touch_down(self, touch):
        if self.row1.collide_point(touch.x, touch.y):
            defender = Defender(self.defenderSelection, 1)
            self.defenderList.append(defender)
            self.row1.addDefender(defender)
        elif self.row2.collide_point(touch.x, touch.y):
            defender = Defender(self.defenderSelection, 2)
            self.defenderList.append(defender)
            self.row2.addDefender(defender)
        elif self.row3.collide_point(touch.x, touch.y):
            defender = Defender(self.defenderSelection, 3)
            self.defenderList.append(defender)
            self.row3.addDefender(defender)
        elif self.row4.collide_point(touch.x, touch.y):
            defender = Defender(self.defenderSelection, 4)
            self.defenderList.append(defender)
            self.row4.addDefender(defender)
        elif self.row5.collide_point(touch.x, touch.y):
            defender = Defender(self.defenderSelection, 5)
            self.defenderList.append(defender)
            self.row5.addDefender(defender)


    #Keyboard input
    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == '1':
            self.defenderSelection = 1
            print("%s" % self.defenderSelection)
        elif keycode[1] == '2':
            self.defenderSelection = 2
            print("%s" % self.defenderSelection)
        elif keycode[1] == '3':
            self.defenderSelection = 3
            print("%s" % self.defenderSelection)

    #taken from Kivy Documentation
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None


#GAMEAPP CLASS
class GameApp(App):
    def build(self):
        game = Game()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    GameApp().run()