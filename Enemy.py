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
    speed = 0

    def __init__(self, selection, row, **kwargs):
        super(Enemy, self).__init__(**kwargs)
        self.row = row
        self.setStats(selection)
        self.loadImage(selection)
        self.set_center_x(Window.width - self.width)
        self.set_center_y(50)

    def setStats(self, selection):
        if selection == 1:
            #Basic enemy
            self.health = 50
            self.power = 5
            self.name = 'enemyGnome'
            self.speed = 10
        elif selection == 2:
            #Strong enemy, weak health
            self.health = 75
            self.power = 10
            self.name = 'enemyTroll'
            self.speed = 6
        elif selection == 3:
            #Fast enemy
            self.health = 80
            self.power = 7
            self.name = 'enemyDragon'
            self.speed = 8

    def loadImage(self, selection):
        try:
            img = os.path.join(os.path.dirname(__file__), 'images', self.name, 'walk0.png')
            self.source = img
        except Exception as e:
            Logger.error("Error loading %s" %img)

    def move(self):
        self.set_center_x(self.get_center_x() - self.speed)

    def update(self, dt):
        self.animDelay += 1
        if self.animDelay >= 10:
            self.animDelay = 0
            self.animCounter += 1
            if self.animCounter >= 8:
                self.animCounter = 0
            if self.state == 1:
                self.source = os.path.join(os.path.dirname(__file__),
                                       'images', self.name, 'walk%d.png' %self.animCounter)
                self.move()
            elif self.state == 2:
                self.source = os.path.join(os.path.dirname(__file__),
                                       'images', self.name, 'attack%d.png' %self.animCounter)
        if self.health <= 0:
            self.state = 3