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
    health = 100
    power = 20
    row = 0
    picture = StringProperty(None)

    def __init__(self, **kwargs):
        super(Character, self).__init__(**kwargs)

    def takeDamage(self, damage):
        self.health -= damage

    def loadImages(self):
        pass

