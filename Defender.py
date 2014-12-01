__author__ = 'Jacob'
"""
2D Game Programming
Project 3
Character Class

This is a the Defender class.  The player selects what Defender they want to select
and what row they want the Defender placed in.

Methods:
init(self, selection, rowNumber, **kwargs)
    Calls the parent class and then initializes the variables inherited from Character.py

setStats(self, selection)
    Given selection, determines what stats to assign the Defender.

loadImage(self, selection)
    Load the given the selected Defender's name assigned in setStats()

update(self, dt)
    Updates the defender's images based on the current state.
"""

from kivy.core.audio import SoundLoader
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
            self.power = 10
            self.cost = 5
            self.name = 'defenderCaveman'
        elif selection == 2:
            self.health = 150
            self.power = 20
            self.cost = 15
            self.name = 'defenderDwarf'
        elif selection == 3:
            self.health = 200
            self.power = 15
            self.cost = 20
            self.name = 'defenderVlad'
        elif selection == 4:
            self.health = 100
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
            if self.animDelay >= 10:
                self.animDelay = 0
                self.animCounter += 1
                if self.animCounter >= 8:
                    self.animCounter = 0
                    sound = SoundLoader.load(os.path.join(os.path.dirname(__file__), 'sounds', 'punch1.wav'))
                    sound.play()
                self.source = os.path.join(os.path.dirname(__file__),
                                           'images', self.name, 'attack%d.png' %self.animCounter)

        if self.health <= 0:
            self.state = 3