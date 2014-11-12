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
import Character, os

class Defender(Image):

    def init(self, **kwargs):
        super(Defender, self).__init__(**kwargs)
        self.loadImage()
        self.set_center_y(50)
        self.set_center_x(50)

    def loadImage(self):
        try:
            img = os.path.join(os.path.dirname(__file__), 'images', 'defender.png')
            self.source = img
        except Exception as e:
            Logger.error("Error loading %s" %img)


    def update(self):
        self.set_center_x(self.get_center_x()+1)
