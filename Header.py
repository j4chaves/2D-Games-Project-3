__author__ = 'Jacob'
"""
2D Game Programming
Project 3
Header Class

This class displays the currently selected Defender and the players current score at the top of the screen.
"""

from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color
import os

class Header(Widget):
    defImage1 = Image()
    defImage2 = Image()
    defImage3 = Image()
    selected1 = Image()
    selected2 = Image()
    selected3 = Image()
    score = Label()

    def __init__(self, **kwargs):
        super(Header, self).__init__(**kwargs)
        self.DefenderMenu()

    def DefenderMenu(self):
        #Load the images for the defender selection
        directory = os.path.dirname(__file__)
        def1FileName = os.path.join(directory, 'images', 'defender1.png')
        def2FileName = os.path.join(directory, 'images', 'defender2.png')
        def3FileName = os.path.join(directory, 'images', 'defender3.png')
        self.defImage1.source = def1FileName
        self.defImage2.source = def2FileName
        self.defImage3.source = def3FileName
        self.defImage1.set_center_x(self.right / 2 - self.defImage1.width - 5)
        self.defImage1.set_center_y(self.top - self.height/2)
        self.defImage2.set_center_x(self.right / 2)
        self.defImage1.set_center_y(self.top - self.height/2)
        self.defImage3.set_center_x(self.right / 2 + self.defImage1.width + 5)
        self.defImage1.set_center_y(self.top - self.height/2)

        self.add_widget(self.defImage1)
        #self.add_widget(self.defImage2)
        #self.add_widget(self.defImage3)

    def on_touch_down(self, touch):
        pass