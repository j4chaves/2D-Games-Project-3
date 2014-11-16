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
from kivy.config import Config              #needed to configure the window size
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.logger import Logger
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
import os
from Defender import Defender
from Enemy import Enemy

#Credit to Mathieu Virbel on https://groups.google.com/forum/#!topic/kivy-users/TR7UycgcLpQ/discussion
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')


"""
TODO
1. Create ROWS and allow selection of ROWS

BUGS

1. When placing Defenders rapidly, the whole game speeds up.  This causes an error hen an enemy needs to be removed from
   the enemyList.  The program can't seem to find the enemy.
"""


#GAME CLASS
class Game(Widget):
    enemySpawnCounter = 0
    defenderList = []
    enemyList = []
    defenderSelection = 1

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        filename = os.path.join(os.path.dirname(__file__), "images", "background.png")

        #Taken from Kivy window Documentation
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down = self.on_keyboard_down)

    #THIS WHOLE METHOD NEEDS TO BE THOUGHT OUT ON PAPER BEFORE BEING IMPLEMENTED
    def update(self, dt):

        for e in self.enemyList:
            if len(self.defenderList) > 0:
                for d in self.defenderList:
                    if e.collide_widget(d):
                        d.takeDamage(e.power)
                        e.takeDamage(d.power)
                    else:
                        e.move()

                    #Remove Defender or Enemy if health is below 0
                    if e.health <= 0:
                        self.enemyList.remove(e)
                        self.remove_widget(e)
                    if d.health <= 0:
                        self.remove_widget(d)
                        self.defenderList.remove(d)
            else:
                e.move()

        #Add new enemy after 3 seconds
        if self.enemySpawnCounter > 180:
            e = Enemy()
            self.enemyList.append(e)
            self.add_widget(e)
            self.enemySpawnCounter = 0
        else:
            self.enemySpawnCounter += 1


    def on_touch_down(self, touch):
        defender = Defender()
        self.defenderList.append(defender)
        self.add_widget(defender)

    #Keyboard input
    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == '1':
            self.defenderSelection = 1
            print("%s" %self.defenderSelection)
        elif keycode[1] == '2':
            self.defenderSelection = 2
            print("%s" %self.defenderSelection)
        elif keycode[1] == '3':
            self.defenderSelection = 3
            print("%s" %self.defenderSelection)

    #taken from Kivy Documentation
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

#GAMEAPP CLASS
class GameApp(App):
    def build(self):
        game = Game()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    GameApp().run()