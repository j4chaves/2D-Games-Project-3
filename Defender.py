__author__ = 'Jacob'
"""
2D Game Programming
Project 3
Character Class

This is a the Defender class.  The player selects what Defender they want to select
and what row they want the Defender placed in.

Methods:
init(self, selection, rowNumber, **kwargs)
setStats(self, selection)
loadImage(self, selection)
update(self, dt)
"""

from kivy.uix.image import Image
from kivy.logger import Logger
from Character import Character
import os

class Defender(Character):

    def __init__(self, selection, rowNumber, **kwargs):
        super(Defender, self).__init__(**kwargs)
        self.row = rowNumber
        self.setStats(selection)
        self.loadImage(selection)

    def setStats(self, selection):
        if selection == 1:
            self.health = 100
            self.power = 25
            self.name = 'defenderCaveman'
        elif selection == 2:
            self.health = 150
            self.power = 20
            self.name = 'defenderDwarf'
        elif selection == 3:
            self.health = 200
            self.power = 13
            self.name = 'defenderVlad'
        elif selection == 4:
            self.health = 20
            self.power = 40

    def loadImage(self, selection):
        try:
            img = os.path.join(os.path.dirname(__file__), 'images', self.name, 'attack0.png')
            self.source = img
        except Exception as e:
            Logger.error("Error loading %s" %img)

    def update(self, dt):
        if self.state == 2:
            self.animDelay += 1
            if self.animDelay >= 30:
                self.animDelay = 0
                self.animCounter += 1
                if self.animCounter >= 8:
                    self.animCounter = 0
                self.source = os.path.join(os.path.dirname(__file__),
                                           'images', self.name, 'attack%d.png' %self.animCounter)