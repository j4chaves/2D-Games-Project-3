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
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.logger import Logger
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
import os
import random
from Defender import Defender
from Enemy import Enemy


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
class Game(GridLayout):
    enemySpawnCounter = 0
    defenderList = []
    enemyList = []
    defenderSelection = 1

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.rows = 6
        filename = os.path.join(os.path.dirname(__file__), "images", "background.png")

        #Taken from Kivy window Documentation
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self.on_keyboard_down)

    #THIS WHOLE METHOD NEEDS TO BE THOUGHT OUT ON PAPER BEFORE BEING IMPLEMENTED
    def update(self, dt):
        #Add new enemy after 3 seconds
        if self.enemySpawnCounter > 180:
            randomEnemy = random.randint(1, 3)
            e = Enemy(randomEnemy)
            self.enemyList.append(e)
            self.add_widget(e)
            self.enemySpawnCounter = 0
        else:
            self.enemySpawnCounter += 1

        for e in self.enemyList:
            for d in self.defenderList:
                if e.collide_widget(d):
                    e.takeDamage(d.power)
                    d.takeDamage(e.power)


    def on_touch_down(self, touch):
        defender = Defender(self.defenderSelection)
        self.defenderList.append(defender)
        self.add_widget(defender)

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