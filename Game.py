__author__ = 'Jacob'
"""
2D Game Programming
Project 3
Game Class

This is the main game file that controls the flow of the game.
"""

from kivy.app import App
from kivy.clock import Clock
from kivy.logger import Logger
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
import os

class Menu(Image):
    def __init__(self, **kwargs):
        super(Menu, **kwargs).__init__(**kwargs)
        self.loadImage()

    def loadImage(self):
        try:
            directory = os.path.dirname(__file__)
            filename = os.path.join(directory, 'images', "background0000.png")
            self.source = filename  #source is inherited from Image class
            self.set_center_x(Window.width / 2)
            self.set_center_y(Window.height / 2)
        except Exception as e:
            Logger.debug("%s could not be loaded" %filename)

class Game(Widget):
    menu = Menu()

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.add_widget(self.menu)

    def update(self):
        print("Something")

class GameApp(App):
    def build(self):
        game = Game()
        #Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    GameApp().run()