__author__ = 'Jacob'
"""
2D Game Programming
Project 3
Character Class

This is a parent class for the Enemy and Defender classes.

Variables:
health - Health of the Character. When it reaches 0, the Character dies.
power - The attack power of the Character.
row - The row that the Character is is in.
state - The current state of the Character.  1 = walking, 2 = attacking.
name - The name of the Character.  Used for file naming purposes
animCounter - Used to determine what picture to display to the screen.
animDelay - Counter used to delay the next picture in the animation.

Methods:
init(self, **kwargs)
    simply calls the parent class __init__

takeDamage(self, damage)
    Subtracts the value of damage from the character's health
"""

from kivy.uix.image import Image
from kivy.properties import StringProperty

class Character(Image):

    #Variables
    health = 100
    power = 20
    row = 0
    state = 1
    name = ""
    animCounter = 0
    animDelay = 0
    image = StringProperty(None)

    def __init__(self, **kwargs):
        super(Character, self).__init__(**kwargs)

    def takeDamage(self, damage):
        self.health -= damage

