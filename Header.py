__author__ = 'Jacob'
"""
2D Game Programming
Project 3
Header Class

This class displays the currently selected Defender and the players current score at the top of the screen.

Variables:
defImage1 - Image for the Caveman Defender
defImage2 - Image for the Dwarf Defender
defImage3 - Image for the Vlad Defender
selected1 - Image for when Caveman is selected for placement
selected2 - Image for when Dwarf is selected for placement
selected3 - Image for when Vlad is selected for placement
score - Player's score
scoreLabel - Label for the player's score
resources - The resources the player has to select defenders
resourceLabel - Label for the amount of player's resources

Methods:
init(self, **kwargs)
    Calls the parent class __init__

DefenderMenu(self)
    Creates the menu for the player to select defenders from.  This method loads the images and sets their coordinates.

ChangeDefenderSelection(self, touch, current)
    This method alters the images of the DefenderMenu to display to the player what defender is currently selected.

scoreInitialization(self)
    Creates the score label and sets the initial score to 0.

updateScore(self, number)
    Updates the players score when an enemy has been killed.

resourceInitialization(self)
    Creates the resource label and sets the coordinates.

updateResources(self, number)
    Updates the resource label to accurately display the amount of resources the player has.

def haveEnoughResources(self, cost)
    Returns a boolean value based on whether or not the player has enough resources to place the
    currently selected defender.
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
    score = 0
    scoreLabel = Label()
    resources = 15
    resourceLabel = Label()

    def __init__(self, **kwargs):
        super(Header, self).__init__(**kwargs)

    def DefenderMenu(self):
        #Load the images for the defender selection
        directory = os.path.dirname(__file__)
        def1FileName = os.path.join(directory, 'images', 'defenderCaveman', 'attack0.png')
        self.defImage1.source = def1FileName
        self.add_widget(self.defImage1)
        self.defImage1.set_center_x(self.right / 2 - self.defImage1.width - 5)
        self.defImage1.set_center_y(self.top - self.height/2)

        def2FileName = os.path.join(directory, 'images', 'defenderDwarf', 'attack0.png')
        self.defImage2.source = def2FileName
        self.add_widget(self.defImage2)
        self.defImage2.set_center_x(self.right / 2)
        self.defImage2.set_center_y(self.top - self.height/2)

        def3FileName = os.path.join(directory, 'images', 'defenderVlad', 'attack0.png')
        self.defImage3.source = def3FileName
        self.add_widget(self.defImage3)
        self.defImage3.set_center_x(self.right / 2 + self.defImage3.width + 5)
        self.defImage3.set_center_y(self.top - self.height/2)

    def changeDefenderSelection(self, touch, current):
        if self.defImage1.collide_point(touch.x, touch.y):
            directory = os.path.dirname(__file__)
            self.defImage1.source = os.path.join(directory, 'images', 'defenderCaveman', 'selected.png')
            self.defImage2.source = os.path.join(directory, 'images', 'defenderDwarf', 'attack0.png')
            self.defImage3.source = os.path.join(directory, 'images', 'defenderVlad', 'attack0.png')
            return 1
        elif self.defImage2.collide_point(touch.x, touch.y):
            directory = os.path.dirname(__file__)
            self.defImage1.source = os.path.join(directory, 'images', 'defenderCaveman', 'attack0.png')
            self.defImage2.source = os.path.join(directory, 'images', 'defenderDwarf', 'selected.png')
            self.defImage3.source = os.path.join(directory, 'images', 'defenderVlad', 'attack0.png')
            return 2
        elif self.defImage3.collide_point(touch.x, touch.y):
            directory = os.path.dirname(__file__)
            self.defImage1.source = os.path.join(directory, 'images', 'defenderCaveman', 'attack0.png')
            self.defImage2.source = os.path.join(directory, 'images', 'defenderDwarf', 'attack0.png')
            self.defImage3.source = os.path.join(directory, 'images', 'defenderVlad', 'selected.png')
            return 3
        else:
            return current

    def changeDefenderSelectionKeyboard(self, key, current):
        if key == 1:
            directory = os.path.dirname(__file__)
            self.defImage1.source = os.path.join(directory, 'images', 'defenderCaveman', 'selected.png')
            self.defImage2.source = os.path.join(directory, 'images', 'defenderDwarf', 'attack0.png')
            self.defImage3.source = os.path.join(directory, 'images', 'defenderVlad', 'attack0.png')
            return 1
        elif key == 2:
            directory = os.path.dirname(__file__)
            self.defImage1.source = os.path.join(directory, 'images', 'defenderCaveman', 'attack0.png')
            self.defImage2.source = os.path.join(directory, 'images', 'defenderDwarf', 'selected.png')
            self.defImage3.source = os.path.join(directory, 'images', 'defenderVlad', 'attack0.png')
            return 2
        elif key == 3:
            directory = os.path.dirname(__file__)
            self.defImage1.source = os.path.join(directory, 'images', 'defenderCaveman', 'attack0.png')
            self.defImage2.source = os.path.join(directory, 'images', 'defenderDwarf', 'attack0.png')
            self.defImage3.source = os.path.join(directory, 'images', 'defenderVlad', 'selected.png')
            return 3
        else:
            return current

    def scoreInitialization(self):
        self.scoreLabel = Label(text='[color=ff3333][b]Score: %d' %self.score + '[/b][/color]', markup = True)
        self.scoreLabel.set_center_x(self.width - 100)
        self.scoreLabel.set_center_y(self.top - 50)
        self.add_widget(self.scoreLabel)

    def updateScore(self, number):
        self.score += number
        self.scoreLabel.text = ('[color=ff3333][b]Score: %d' %self.score + '[/b][/color]')

    def resourceInitialization(self):
        self.resourceLabel = Label(text='[color=ff3333][b]Resources: %d' %self.resources + '[/b][/color]', markup = True)
        self.resourceLabel.set_center_x(100)
        self.resourceLabel.set_center_y(self.top - 50)
        self.add_widget(self.resourceLabel)

    def updateResources(self, number):
        self.resources += number
        self.resourceLabel.text =('[color=ff3333][b]Resources: %d' %self.resources + '[/b][/color]')

    def haveEnoughResources(self, cost):
        if self.resources >= cost:
            self.updateResources(cost * (-1))
            return True
        else:
            return False