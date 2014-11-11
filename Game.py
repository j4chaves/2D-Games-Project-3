__author__ = 'Jacob'
"""
2D Game Programming
Project 3
Game Class

This is the main game file that controls the flow of the game.
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock

class Game(Widget):
    pass

class GameApp(App):
    game = Game()
    Clock.shedule_update(game.update, 1.0/60.0)
    return game

if __name__ == '__main__':
    GameApp.run()