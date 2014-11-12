__author__ = 'Jacob'
"""
2D Game Programming
Project 3
Character Class

This is a parent class for the Enemy and Defender classes.
"""

from kivy.uix.image import Image
from kivy.properties import StringProperty

class Character(Image):

    #Variables
    health = 0
    row = 0
    picture = StringProperty(None)

    def init(self, **kwargs):
        pass#super(Character, self).__init__(**kwargs)

    def loadImages(self):
        pass

    def update(self):
        self

