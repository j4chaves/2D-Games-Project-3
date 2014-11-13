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

    def __init__(self, **kwargs):
        super(Enemy, self).__init__(**kwargs)
        self.loadImage()
        self.set_center_x(Window.width - self.width)
        self.set_center_y(50)

    def loadImage(self):
        try:
            img = os.path.join(os.path.dirname(__file__), 'images', 'enemy.png')
            self.source = img
        except Exception as e:
            Logger.error("Error loading %s" %img)

    def update(self, collided):
        #Needs to be thought out/reworked
        if collided == True:
            pass
        else:
            self.set_center_x(self.get_center_x() - 1)
