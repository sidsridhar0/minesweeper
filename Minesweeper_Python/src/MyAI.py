# ==============================CS-199==================================
# FILE:			MyAI.py
#
# AUTHOR: 		Justin Chung
#
# DESCRIPTION:	This file contains the MyAI class. You will implement your
#				agent in this file. You will write the 'getAction' function,
#				the constructor, and any additional helper functions.
#
# NOTES: 		- MyAI inherits from the abstract AI class in AI.py.
#
#				- DO NOT MAKE CHANGES TO THIS FILE.
# ==============================CS-199==================================
# TODO: Implement the real algorithm that could solve the whole problem

# TODO: Make some kind of mock up algorithm so we could pass the first time check
"""
For the mock up algorihm, I will only put those safe tiles in the frontier and
don't use the real algorithm to check for probabilities.(Those could be done
later)
"""


# TODO List:
"""
1. design tile class(working on right now)
2. In any situation, explore all safe square before start calculate possibilty until no safe square
3. If the tile have the same amount of hidden square around it as unflagged bombs remaining around it then all hidden tiles are bomb.(implement)
4. If a tile has the same amount of flags around it as the number in the square, then all remaining hidden tiles are not bomb.(implement)	
5. When 3, 4 won't be able to detect any safe tile, use another algorithm to decide what to search next(to be decide, might be mine arrangement)
"""

#* use mine arrangement to solve the problem
'''
generate models of frontier that is possible with current information. 
1.write is_valid function to check whether arrangement is possible
2.write generate_arrangement function with frontier and total mine number
3.calculate the possiblity of each tile being mine

#? The algorithm could be very slow since it will generate a lot of arrangement and test them
'''

#* some rules about minesweeper
'''
1. Last uncover tile may affect the possibility of more than just adjacent tiles being mine.
2. According to youtube video, mines in different section won't affect each other.
3. The possiblity of mine could be calculated by using mine arragement.(not sure how to write the algorithm)
4. If the tile have the same amount of hidden square around it as unflagged bombs remaining around it then all hidden tiles are bomb.
5. If a tile has the same amount of flags around it as the number in the square, then all remaining hidden tiles are not bomb.	
'''

#? at the beginnning of the game, should we just uncovered the four corners?

#! maybe use some kind of combination of the two algorithm

from AI import AI
from Action import Action


class MyAI( AI ):

	def __init__(self, rowDimension, colDimension, totalMines, startX, startY):

		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		#? not sure about whether to store possiblity of mine or just init value as 0			
		self._rowDimension = rowDimension
		self._colDimension = colDimension
		self._board = dict()          #* initialize board as empty. dict((pos_x, pos_y) : Tile objcet)
		self._unvisited = set()      #* keep record of unvisited tiles 
		self._last_visited = (startX,startY)  #* keep record of last visited tile
		self._last_action = 1     #* record last action as 1, which is uncover. last action as -1 means last action was flag or unflag a tile.
		self._safe = []           #* keep track of safe tiles on frontier to explore
		self._visited = set()    #* keep track of visited tiles
		self._mine_num = totalMines
		self._flagged_tiles = set()  #* keep track of flagged tiles
		self._mines = set()
		#* keep track of tiles adjacent to all visited frontier since they are 
		#* the tiles that will be choosed to explore.
		self._frontier = dict()  #* dict((pos_x, pos_y) : Tile objcet

		self.create_board()

		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################

		
	def getAction(self, number: int) -> "Action Object":
		'''
		# this function will be called by World.run
		The "number" parameter is the result of last visited squre. When teh game start, 
		the number passed will be the first revealed tile. 
		1.The number will be the number of tile uncovered if last action is uncover 
		2.The number will be -1 if last action is place a flag or unplace a flag
		'''

		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		if self._last_action == 1:
			self.uncover_tile(self._last_visited[0],self._last_visited[1],number)
			#! not finished

		return Action(AI.Action.LEAVE)
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################
	
	
	def process_tile(self ,x_pos: int ,y_pos :int) -> None:
		'''
		This function process a tile and assign differnt value to tiles
		adjacent to position.
		'''		
		
		pass
	
	#? not sure about where to use this function and how to use it. I think
	#? we could use this function to calculate the possiblity of a tile being
	#? 0 and put it to safe list when that happens.
	def calculate_possibility_for_tile(self ,x_pos: int ,y_pos :int) -> int:
		'''
		This fucntion calculate the possibility of a tile being mine,
		The possibility will be between 0 and 1
		'''

		#stub
		return 0

	
	def create_board(self) -> None:
		for row in range(1,self._rowDimension + 1):
			for col in range(1, self._colDimension + 1):
				self._board[(row,col)] = Tile(row,col)
				self._unvisited.add((row,col))

	#* I kind of feel like this is the core function.	
	def uncover_tile(self, x_pos:int , y_pos :int ,number :int)->None:
		self._unvisited.pop((x_pos, y_pos))
		self._last_visited = tuple(x_pos, y_pos)
		self._last_action = 1
		self._visited[(x_pos, y_pos)] = number

		#! unfinished
		# start to change status after uncovering a tile
		self._frontier = list() 
		

	def adjacent_tiles(self, x_pos:int , y_pos :int) -> "[(x_pos, y_pos),]":
		x_pos_start = x_pos - 1
		y_pos_start = y_pos - 1

		adjacent_tiles_list = []
		
		for row in range(x_pos_start, x_pos_start + 3):
			for col in range(y_pos_start, y_pos_start + 3):
				if self.in_bound(row,col):
					adjacent_tiles_list.append(tuple(row,col))
		
		adjacent_tiles_list.remove(tuple(x_pos, y_pos))

		return adjacent_tiles_list

	def in_bound(self, x_pos:int , y_pos :int) -> bool:
		if x_pos >= 1 and x_pos <= self.rowDimension:
			if y_pos >= 1 and y_pos <= self.colDimension:
				return True

		return False

class Tile:
	def __init__(self, pos_x, pos_y) -> None:
		self.pos_x = pos_x 
		self.pos_y = pos_y
		self.explored = False
		self.adjacent_mine_num = 0
		self.flagged = False
		self.is_mine = False
		self.possibilty = 0

	def assign_number(self, number):
		self.adjacent_mine_num = number
	
	def assign_mine(self):
		self.is_mine = True
	
	def assign_flag(self):
		self.flagged = True
	
	def assign_explored(self):
		self.explored = True
	
	def assign_possibility(self, possibility):
		self.possibilty = possibility

	def assign_adjacent_mine_num(self, number):
		self.adjacent_mine_num = number