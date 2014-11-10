__author__ = 'Jacob'
"""
2D Game Programming
Project 3
Character Class

This is a parent class for the Enemy and Defender classes.
"""

from kivy.uix.image import Image
from kivy.properties import StringProperty

class Character:

    #Variables
    health = 0
    picture = StringProperty(None)

    def init(self):
        pass

    def loadImages(self):
        pass

