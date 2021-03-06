#!/usr/bin/env python2
import random

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
		for y in range(self.height):
			for x in range(self.width):
				if fill == "random":
					self.CellsDict[x,y] = Cell( x, y, random.choice([True,False]) )
				elif fill == "blank":
					self.CellsDict[x,y] = Cell( x, y, False )
				elif fill == "full":
					self.CellsDict[x,y] = Cell( x, y, True )
	def fillWeightedRandom(self,weight):
		# fills the board, with weight-chance of life in each cell
		# 0.0 means empty board, 1.0 means full board
		weight = float(weight) # just in case
		for x in range(self.width):
			for y in range(self.height):
				if random.random() < weight:
					self.CellsDict[x,y] = Cell( x, y, True )
				else:
					self.CellsDict[x,y] = Cell( x, y, False )
	def isLifeAt(self,x,y):
		# returns True if the cell at x,y is alive
		# otherwise, returns false
		return self.CellsDict[x,y].life
	def __repr__(self):
		return self.toString()
	def toString(self,xSpacing=" ",ySpacing="\n",trailingNewline=True):
		# converts the board to a multi-line string
		# use xSpacing on rows, and ySpacing on columns
		life = self.IconLife
		nope = self.IconNoLife
		boardString = ""
		for y in range(self.height):
			for x in range(self.width):
				cellLife = self.isLifeAt(x,y)
				if cellLife:
					boardString = xSpacing.join([boardString,self.IconLife])
				elif not cellLife:
					boardString = xSpacing.join([boardString,self.IconNoLife])
			boardString = ''.join([boardString,ySpacing])
		if trailingNewline:
			return boardString
		elif not trailingNewline:
			return boardString[:-1]
	def printAsString(self,xSpacing=" ",ySpacing="\n"):
		print self.toString(xSpacing=xSpacing,ySpacing=ySpacing)
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
		newCellsDict = {}
		for cell in self.CellsDict:
			cell_x = self.CellsDict[cell].Position_x
			cell_y = self.CellsDict[cell].Position_y
			cell_life = self.WillCellBeAliveNextRound(cell_x,cell_y)
			newCellsDict[cell_x,cell_y] = Cell(cell_x, cell_y, cell_life)
		self.CellsDict = newCellsDict
	def writeToFile(self,output):
		# writes the current board to the file "output", formatted as a string
		# make sure not to set IconNoLife to " " if you use this
		toWrite = self.toString(xSpacing="",trailingNewline=False)
		with open(output,'w') as outputFile:
			outputFile.write(toWrite)
	def readFromFile(self,inputFile):
		# reads a board from the given file, and imports it to this board.
		self.CellsDict = {}
		with open(inputFile) as importFile:
			# determine the width and height of the board from the file
			self.height = len(importFile.readlines())
			importFile.seek(0)
			self.width = len(importFile.readline().strip('\n'))
			importFile.seek(0)
			# this is complicated and difficult to understand.
			# but it was the only way I could get it to work
			for line,y in zip(importFile.readlines(),xrange(self.height)):
				for cell,x in zip(line,xrange(self.width)):
					if cell == self.IconLife:
						cellLife = True
					elif cell == self.IconNoLife:
						cellLife = False
					self.CellsDict[x,y] = Cell(x,y,cellLife)
	def shrink(self,x,y):
		# shrinks the board to size x, y
		newCellsDict = {}
		# remove old cells
		for cell in self.CellsDict:
			cell_x = self.CellsDict[cell].Position_x
			cell_y = self.CellsDict[cell].Position_y
			if cell_x <= x and cell_y <= y:
				newCellsDict[cell] = self.CellsDict[cell]
		# new size
		self.width = x
		self.height = y
		self.CellsDict = newCellsDict
	def shift(self,x,y,fill="blank"):
		# shifts the board by x, y
		# these values may be negative
		# cells that land outside the grid will be removed.
		newCellsDict = {}
		for cell in self.CellsDict:
			cell_x = self.CellsDict[cell].Position_x
			cell_y = self.CellsDict[cell].Position_y
			# cell_life = self.CellsDict[cell].Life
			cell_x += x
			cell_y += y
			newCellsDict[cell_x,cell_y] = self.CellsDict[cell]
		for y in xrange(self.height):
			for x in xrange(self.width):
				if not (x,y) in newCellsDict:
					if fill == "random":
						newCellsDict[x,y] = Cell( x, y, random.choice([True,False]) )
					elif fill == "blank":
						newCellsDict[x,y] = Cell( x, y, False )
					elif fill == "full":
						newCellsDict[x,y] = Cell( x, y, True )
		self.CellsDict = newCellsDict
	def expand(self,x,y,fill="blank"):
		# expand the board to the size x, y
		# if the board is larger than x, y, return False
		if x > self.width or y > self.height: 
			return False
		self.width  = x 
		self.height = y
		for y in xrange(self.height):
			for x in xrange(self.width):
				if not (x,y) in self.CellsDict:
					if fill == "random":
						self.CellsDict[x,y] = Cell( x, y, random.choice([True,False]) )
					elif fill == "blank":
						self.CellsDict[x,y] = Cell( x, y, False )
					elif fill == "full":
						self.CellsDict[x,y] = Cell( x, y, True )
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
