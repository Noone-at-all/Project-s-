#!/usr/bin/env python2
import random
import pygame
#############################
### Conway's Game of Life ###
#############################
# http://en.wikipedia.org/wiki/Conway's_Game_of_Life#Rules
# Rules: 
# 1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
# 2. Any live cell with two or three live neighbours lives on to the next generation.
# 3. Any live cell with more than three live neighbours dies, as if by overcrowding.
# 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

class Board(object):
	def __init__(self,x,y,fill="random"):
		# creates a board object that is x columns wide by y rows tall
		# possible fill values are:
		#	"random"
		# 	"blank"
		# 	"full"
		self.width = x
		self.height = y
		self.IconLife = "#"
		# self.IconNoLife = "0"
		self.IconNoLife = "-"
		self.CellsDict = {}
		for x in range(self.width):
			for y in range(self.height):
				if fill == "random":
					self.CellsDict[x,y] = Cell( x, y, random.choice([True,False]) )
				elif fill == "blank":
					self.CellsDict[x,y] = Cell( x, y, False )
				elif fill == "full":
					self.CellsDict[x,y] = Cell( x, y, True )
	def isLifeAt(self,x,y):
		# returns True if the cell at x,y is alive
		# otherwise, returns false
		return self.CellsDict[x,y].life
	def __repr__(self):
		# converts the board to a multi-line string
		life = self.IconLife
		nope = self.IconNoLife
		# build the string by joining it to itself
		# use spaces on rows, and newlines on columns 
		boardString = ""
		for x in range(self.width):
			for y in range(self.height):
				cellLife = self.isLifeAt(x,y)
				if cellLife:
					boardString = ' '.join([boardString,self.IconLife])
				elif not cellLife:
					boardString = ' '.join([boardString,self.IconNoLife])
			boardString = ''.join([boardString,'\n'])
		return boardString
	def printAsString(self):
		print self
	def CountLivingNeighbors(self, x, y):
		# counts how many neighbor cells of the cell at x, y are living
		neighbors = 0
		for column in xrange(x-1,x+2):
			for row in xrange(y-1,y+2):
				if not (column,row) == (x,y): # so we don't count the given cell
					# tries to do all 8 bordering cells, and soft-fails if a cell does not exist
					# (which could happen if the given coordinates are on the border)
					try:
						if self.isLifeAt(column,row):
							neighbors += 1
					except:
						pass
		return neighbors
	def WillCellBeAliveNextRound(self, x, y):
		# determine whether the cell at x, y will be alive next round
		# this code is modified from dav's original function elsewhere
		LivingNeighbors = self.CountLivingNeighbors(x,y)
		if LivingNeighbors < 2:
			return False
		if LivingNeighbors == 3:
			return True
		if LivingNeighbors > 3:
			return False
		if LivingNeighbors == 2:
			return self.isLifeAt(x,y)
	def advance(self):
		# advances the game one move forward
		# a new cells dictionary is necessary because without it, the results of previous outcomes can effect new outcomes mid-round
		self.newCellsDict = {}
		for cell in self.CellsDict:
			cell_x = self.CellsDict[cell].Position_x
			cell_y = self.CellsDict[cell].Position_y
			cell_life = self.WillCellBeAliveNextRound(cell_x,cell_y)
			self.newCellsDict[cell_x,cell_y] = Cell(cell_x, cell_y, cell_life)
		self.CellsDict = self.newCellsDict

class Cell(object):
	def __init__(self, x, y, life):
		# x and y are the co-ordinates of the cell
		# Life is a bool value,
		self.Position_x = x
		self.Position_y = y
		self.life = life
		if life:
			CoLi = '#'
		elif not life:
			CoLi = 'O'
		self.CoLi = CoLi
	def __repr__(self):
		return "{life}, and at ({x}, {y})".format(life=str(self.life), x=str(self.Position_x), y=str(self.Position_y))

# below this line is temp stuff, for testing.
# currently, it makes a random board that is 5x5, prints it, and then advances it 2 rounds, printing it after each round
brd = Board(5,5,fill="random")
brd.printAsString()
brd.advance()
brd.printAsString()
brd.advance()
brd.printAsString()