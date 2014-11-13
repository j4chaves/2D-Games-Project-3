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
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
import os
from Defender import Defender
from Enemy import Enemy



#GAME CLASS
class Game(Widget):
    enemySpawnCounter = 0
    defenderList = []
    enemyList = []

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        filename = os.path.join(os.path.dirname(__file__), "images", "background.png")


    #THIS WHOLE METHOD NEEDS TO BE THOUGHT OUT ON PAPER BEFORE BEING IMPLEMENTED
    def update(self, dt):

        #Update all the Defenders on the screen
        for d in self.defenderList:
            d.update()

        #Update all the Enemies on the screen
        for e in self.enemyList:
            for d in self.defenderList:
                if d.health <= 0:
                    self.defenderList.remove(d)
                    self.remove_widget(d)

                if e.collide_widget(d):
                    e.update(True)
                    e.takeDamage(d.power)
                    d.takeDamage(e.power)
                else:
                    e.update(False)

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

#GAMEAPP CLASS
class GameApp(App):
    def build(self):
        game = Game()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    GameApp().run()