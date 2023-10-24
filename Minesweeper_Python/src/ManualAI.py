# ==============================CS-199==================================
# FILE:			ManualAI.py
#
# AUTHOR: 		Justin Chung
#
# DESCRIPTION:	This file contains the ManualAI class. This class allows
#				the user to play Minesweeper manually, instead of using
#				an agent. This mode should be used to familiarize your-
#				self with the game and its mechanics.
#
# NOTES: 		- List of actions/commands can be found in Action.py
#
#				- This agent is run using the -m flag
#
#				- DO NOT MAKE CHANGES TO THIS FILE.
# ==============================CS-199==================================

from AI import AI
from Action import Action


class ManualAI( AI ):

	def getAction(self, number: int) -> "Action Object":
		""" Prompt user for type of action, and the coordinates of where to perform that action """
		""" Return an Action object storing that information """
	
		action = AI.Action.UNCOVER		

		#original node
		# action = input("Enter an action: ").strip().lower()		
		# elif action == "u":
			
		# elif action == "f":
		# 	action = AI.Action.FLAG
		# elif action == "n":
		# 	action = AI.Action.UNFLAG
			
		x = input("Enter tuple like (1,1)\n").split()
		# coordX = int(input("Enter the X coordinate of the tile: ").strip()) - 1
		# coordY = int(input("Enter the Y coordinate of the tile: ").strip()) - 1

		# return Action(action, coordX, coordY)
		return Action(action, int(x[0]) - 1, int(x[1]) - 1)
