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
from kivy.uix.image import Image
from kivy.uix.widget import Widget
import os
import Defender


#GAME CLASS
class Game(Widget):
    defenderList = []

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        filename = os.path.join(os.path.dirname(__file__), "images", "background.png")
        print(filename)


    def update(self, dt):
        for d in self.defenderList:
            d.update()

    def on_touch_down(self, touch):
        defender = Defender.Defender()
        self.defenderList.append(defender)
        self.add_widget(defender)

#GAMEAPP CLASS
class GameApp(App):
    def build(self):
        game = Game()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    GameApp().run()