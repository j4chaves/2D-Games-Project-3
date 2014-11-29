__author__ = 'Jacob'
"""
2D Game Programming
Project 3
Row Class

This class separates the rows for which Defenders can be placed and enemies can traverse.

Methods:
addDefender(self, defender) -
addEnemy(self, enemy) -
"""

from kivy.uix.widget import Widget
from kivy.graphics import Color
from Defender import Defender

class Row(Widget):
    def __init__(self, **kwargs):
        super(Row, self).__init__(**kwargs)

    def addDefender(self, defender):
        center = self.get_top() - self.height/2
        defender.set_center_y(center)
        defender.set_center_x(defender.width)
        self.add_widget(defender)

    def addEnemy(self, enemy):
        center = self.get_top() - self.height/2
        enemy.set_center_y(center)
        enemy.set_center_x(self.get_right() - enemy.width)
        self.add_widget(enemy)