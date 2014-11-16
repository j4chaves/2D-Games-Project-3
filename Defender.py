__author__ = 'Jacob'
"""
2D Game Programming
Project 3
Character Class

This is a the Defender class.  The player selects what Defender they want to select
and what row they want the Defender placed in.
"""

from kivy.uix.image import Image
from kivy.logger import Logger
from Character import Character
import os

class Defender(Character):

    def __init__(self, selection, **kwargs):
        super(Defender, self).__init__(**kwargs)
        self.loadImage(selection)
        self.set_center_y(50)
        self.set_center_x(50)

    def loadImage(self, selection):
        try:
            img = os.path.join(os.path.dirname(__file__), 'images', 'defender%d.png' %selection)
            self.source = img
        except Exception as e:
            Logger.error("Error loading %s" %img)