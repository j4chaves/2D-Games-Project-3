__author__ = 'Jacob Chaves'
"""
2D Game Programming
Project 3
Game Class

This is the main game file that controls the flow of the game.

GAME CLASS:
    This class controls the main game mechanics and what is happening on screen.

    VARIABLES:
        charList - list of all the Defenders on the screen
        enemyList - list of all the Enemies of the screen


    METHODS:

GAMEAPP CLASS:
    Top level class that starts the game and the Clock for updating the screen and handles the game logic.
"""

from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config  # needed to configure the window size
from kivy.core.window import Window, WindowBase
from kivy.graphics import Color
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.logger import Logger
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
import os
import random
from Defender import Defender
from Enemy import Enemy
from Header import Header
from Row import Row


"""
TODO
Figure out how to call header.DefenderMenu after init is done but not called continuously
1. Create Win/Loss scenarios
2. Rewrite Game.update() method.  The logic needs to be worked out
3. Implement a Main Menu and 2nd level
4. Animations
6. Comment the files
7. Write Documentation


Variables:
enemySpawnCounter
defenderList
enemyList
enemyTimer
defenderSelection
header
row1
row2
row3
row4
row5
headerIsLoaded

Methods:
init(self, **kwargs)
    Initializes the Game window.  This method sets the orientation for the boxLayout (which Game inherits from), adds
    the header and the 5 rows, and creates a binding for keyboard input.

update(self, dt)

removeCharacter(self, character)
    Removes the given character (defender or enemy) from their corresponding list and then removes their widget from
    whatever row they were in.  If an Enemy was removed, then the player's score is increased by 5.

on_touch_down(self, touch)
    First the method checks if the currently selected defender's cost is more than what the player has.  Then, it
    checks where the mouse click occured.  If it occured in the header, then the currently selected defender is changed.
    If it occured in a row, then if the player has enough resources, a new defender is created and placed.

on_keyboard_down(self, keyboard, keycode, text, modifiers)
    Alters the currently selected defender if '1', '2', or '3' is pressed.  Currently, it does not alter the defender
    menu at the top of the screen.

_keyboard_close(self)
    Removes the keyboard binding.
"""


# GAME CLASS
class Game(BoxLayout):
    enemySpawnCounter = 0
    defenderList = []
    enemyList = []
    enemyTimer = 0
    enemyCounter = 0
    enemiesDefeated = 0
    defenderSelection = 1
    header = Header()
    row1 = Row()
    row2 = Row()
    row3 = Row()
    row4 = Row()
    row5 = Row()
    resources = 5
    score = 0
    headerIsLoaded = False

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(self.header)
        self.add_widget(self.row1)
        self.add_widget(self.row2)
        self.add_widget(self.row3)
        self.add_widget(self.row4)
        self.add_widget(self.row5)

        #Taken from Kivy window Documentation
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self.on_keyboard_down)

    #THIS WHOLE METHOD NEEDS TO BE THOUGHT OUT ON PAPER BEFORE BEING IMPLEMENTED
    def update(self, dt):

        #Add new enemy every 3 seconds, change to 5 seconds later
        self.enemyTimer += dt
        if self.enemyTimer > 5:
            self.header.updateResources(5) #Resources added every 5 seconds, no need for another counter
            self.enemyTimer = 0
            #Generate random numbers to determine which enemy to select and what row to place them in.
            #The enemyNumber is weighted in favor of the weaker enemy type
            enemyNumber = random.randint(1, 10)
            enemyRow = random.randint(1, 5)
            if enemyNumber <= 7:
                enemyNumber = 1
            else:
                enemyNumber = 2
            if not self.enemyCounter >= 15:
                enemy = Enemy(enemyNumber, enemyRow)
                self.enemyList.append(enemy)
                self.enemyCounter += 1

                #Add enemy to their row
                if enemyRow == 1:
                    self.row1.addEnemy(enemy)
                elif enemyRow == 2:
                    self.row2.addEnemy(enemy)
                elif enemyRow == 3:
                    self.row3.addEnemy(enemy)
                elif enemyRow == 4:
                    self.row4.addEnemy(enemy)
                elif enemyRow == 5:
                    self.row5.addEnemy(enemy)

        #Check for whether or not the Defenders or Enemies should be attacking
        for e in self.enemyList:
            for d in self.defenderList:
                if e.row == d.row and d.collide_widget(e):
                    e.state = 2
                    d.state = 2
                    if e.animCounter == 7:
                        d.takeDamage(e.power)
                    if d.animCounter == 7:
                        e.takeDamage(d.power)


        #Update the Defenders and Enemies.  If they are dead, they need to be removed entirely
        for e in self.enemyList:
            e.update(dt)
            if e.state == 3:
                self.removeCharacter(e)
                self.enemiesDefeated += 1
                if self.enemiesDefeated >= 15:
                    #Enact win event here
                    pass
            elif e.get_center_x() <= 0:
                #Enact Losing scenario
                    pass

        for d in self.defenderList:
            d.update(dt)
            if d.state == 3:
                self.removeCharacter(d)

        #Load the header.  Reasoning for being here is in readme file.
        if not self.headerIsLoaded:
            self.header.DefenderMenu()
            self.header.scoreInitialization()
            self.header.resourceInitialization()
            self.headerIsLoaded = True

    def removeCharacter(self, character):
        #Remove the character from the appropriate list
        if isinstance(character, Enemy):
            self.enemyList.remove(character)
            self.header.updateScore(5)
        else:
            self.defenderList.remove(character)

        #Determine the character's row and remove the widget
        if character.row == 1:
            self.row1.remove_widget(character)
        elif character.row == 2:
            self.row2.remove_widget(character)
        elif character.row == 3:
            self.row3.remove_widget(character)
        elif character.row == 4:
            self.row4.remove_widget(character)
        else:
            self.row5.remove_widget(character)

    def on_touch_down(self, touch):
        if self.defenderSelection == 1:
            resourceCost = 5
        elif self.defenderSelection == 2:
            resourceCost = 15
        else:
            resourceCost = 20

        #Change defender selection by clicking on the image in the header
        if self.header.collide_point(touch.x, touch.y):
            self.defenderSelection = self.header.changeDefenderSelection(touch, self.defenderSelection)
        elif self.header.haveEnoughResources(resourceCost):
            if self.row1.collide_point(touch.x, touch.y):
                defender = Defender(self.defenderSelection, 1)
                self.defenderList.append(defender)
                self.row1.addDefender(defender)
            elif self.row2.collide_point(touch.x, touch.y):
                defender = Defender(self.defenderSelection, 2)
                self.defenderList.append(defender)
                self.row2.addDefender(defender)
            elif self.row3.collide_point(touch.x, touch.y):
                defender = Defender(self.defenderSelection, 3)
                self.defenderList.append(defender)
                self.row3.addDefender(defender)
            elif self.row4.collide_point(touch.x, touch.y):
                defender = Defender(self.defenderSelection, 4)
                self.defenderList.append(defender)
                self.row4.addDefender(defender)
            elif self.row5.collide_point(touch.x, touch.y):
                defender = Defender(self.defenderSelection, 5)
                self.defenderList.append(defender)
                self.row5.addDefender(defender)

    #Keyboard input
    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == '1':
            self.defenderSelection = 1
            print("%s" % self.defenderSelection)
        elif keycode[1] == '2':
            self.defenderSelection = 2
            print("%s" % self.defenderSelection)
        elif keycode[1] == '3':
            self.defenderSelection = 3
            print("%s" % self.defenderSelection)

    #taken from Kivy Documentation
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None


#GAMEAPP CLASS
class GameApp(App):
    def build(self):
        game = Game()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game
        #mainMenu = MainMenu()
        #mainMenu.createMenu()
        #return mainMenu


if __name__ == '__main__':
    GameApp().run()