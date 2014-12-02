Jacob Chaves
2D Game Programming #3
Using Python 3.4

How to run:
	This project can be run from either within the Pycharm IDE or from the command line. In order to run from the
	command line, navigate to the directory containing the file "Game.py" and execute the command
	"python ZombieSmash.py" from the command line.

Playing the game:
	The game works similar to Plants vs. Zombies.  Enemies will spawn every 5 seconds and move from the right side of
	the screen to the left.  Every 5 seconds the player also gets 5 more resources to spend on Defenders.  From left to
	right, the Defenders are Caveman, Dwarf, and Vlad.  Caveman defenders cost 5 resources, have 100 health and 10
	attack power. Dwarves cost 10 resources, have 150 health, and 20 attack power. Vlads cost 15 resources, have 200
	health, and 15 attack power.  When the enemy collides with a Defender(when they are both in the same row) they both
	attack each other and the dying one disappears.  Players can choose what Defender they want to select from the
	header.  Alternatively, the player can also use the keys '1', '2', and '3' to select Caveman, Dwarf, or Vlad
	respectively.  For the currently implemented enemies, there is a gnome and a troll.  The gnome is fast and weak
	while the troll is strong and fast.

How I created it:
    For this project I split up the code into multiple classes.  The Defender and Enemy classes are self-explanatory
    and both inherit from Character.  Row is for the rows that the Defenders and Enemies occupy.  Header class is
    similar to Row except it is for choosing between the Defenders.  Currently, the MainMenu is not working.  It was
    planned to be used for selecting between level 1 and level 2.  Due to time, it along with level 2 are not in
    working order.


Left Undone:
    Main Menu implementation
    Second level(I have an additional enemy that would be simple to implement)
    Enemies and Defenders become stuck in attack state once they enter it(if an enemy kills a defender, it won't resume
    walking to the edge of the screen)
    Defenders can only be placed on top of each other, instead of (more desirably) in front of each other
    Caveman's attack is currently melee instead of being a projectile (thrown spear)


Credits:
All images are created by Reiner's tilesets.
All audio was created by Mike Alberto.