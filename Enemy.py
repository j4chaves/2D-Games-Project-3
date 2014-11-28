__author__ = 'Jacob'
"""
2D Game Programming
Project 3
Character Class

This is the Enemy class.  It is the computer controlled characters
that will be traveling from the right side of the screen to the left
and attack the Defenders.
"""

from kivy.properties import Property
from kivy.uix.image import Image
from kivy.logger import Logger
from Character import Character
from kivy.core.window import Window
import os

class Enemy(Character):

    def __init__(self, selection, row, **kwargs):
        super(Enemy, self).__init__(**kwargs)
        self.loadImage(selection)
        self.row = row
        self.setStats(selection)
        self.set_center_x(Window.width - self.width)
        self.set_center_y(50)

    def setStats(self, selection):
        if selection == 1:
            #Basic enemy
            self.health = 100
            self.power = 5
        elif selection == 2:
            #Strong enemy, weak health
            self.health = 60
            self.power = 15
        elif selection == 3:
            #Fast enemy
            self.health = 80
            self.power = 7

    def loadImage(self, selection):
        try:
            img = os.path.join(os.path.dirname(__file__), 'images', 'enemy%d.png' %selection)
            self.source = img
        except Exception as e:
            Logger.error("Error loading %s" %img)

    def move(self):
        self.set_center_x(self.get_center_x() - 10)
