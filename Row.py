__author__ = 'Jacob'
"""
2D Game Programming
Project 3
Row Class

This class separates the rows for which Defenders can be placed and enemies can traverse.
"""

from kivy.uix.widget import Widget

class Row(Widget):
    def __init__(self, **kwargs):
        super(Image, self).__init__(**kwargs)
