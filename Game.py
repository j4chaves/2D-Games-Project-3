__author__ = 'Jacob'
"""
2D Game Programming
Project 3
Game Class

This is the main game file that controls the flow of the game.
"""

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.widget import Widget
import os

class Game(Widget):
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        filename = os.path.join(os.path.dirname(__file__), "images", "background.png")
        self.add_widget(Image(
                source=filename,
                size_hint=(.5, .5),
                pos_hint={'center_x': .5, 'center_y': .5}))
        print(filename)


    def update(self):
        print("Something")

class GameApp(App):
    def build(self):
        game = Game()
        #Clock.schedule_interval(game.update, 1.0/60.0)
        return game

if __name__ == '__main__':
    GameApp().run()