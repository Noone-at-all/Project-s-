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
		self.IconNoLife = "0"
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
					boardString = ' '.join([boardString,"#"])
				elif not cellLife:
					boardString = ' '.join([boardString,"0"])
			boardString = ''.join([boardString,'\n'])
		return boardString
	def printAsString(self):
		print self
	def CountLivingNeighbors(self, x, y):
		# counts how many neighbor cells of the cell at x, y are living
		# TODO
		pass
	def WillCellBeAliveNextRound(self, x, y):
		# determine whether the cell at x, y will be alive next round
		# TODO
		pass
	def advance(self):
		# advances the game one move forward
		# self.newCellsDict = self.CellsDict
		self.newCellsDict = {}
		for cell in self.CellsDict:
			cell_x = self.CellsDict[cell].Position_x
			cell_y = self.CellsDict[cell].Position_y
			cell_life = self.CellsDict[cell].WillBeAliveNextRound()
			self.newCellsDict[cell_x,cell_y,cell_life]
		self.CellsDict = self.newCellsDict
		# this doesn't work yet, because several functions still depend on global variables

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
	# def __repr__(self):
	# 	return "{life}, and at ({x}, {y})".format(life=str(self.life), x=str(self.Position_x), y=str(self.Position_y))
	def WillBeAliveNextRound(self):
		# this function doesn't work, because CountLivingNeighbors doesn't work, because CountLivingNeighbors depends on obsolete global variables
		# returns True or False depending on whether this cell should be alive the next round
		LivingNeighbors = CountLivingNeighbors(self.Position_x, self.Position_y)
		if LivingNeighbors < 2:
			self.life = False
		if LivingNeighbors == 3:
			self.life = True
		if LivingNeighbors > 3:
			self.life = False
		if LivingNeighbors == 2:
			self.life = self.life

# this needs to be re-written, and moved to a Board() method
def CountLivingNeighbors(x, y):
	# this doesn't work, because it depends on obsolete global variables
	count = 0
	Gatex = False
	Gatey = False
	if x > 0:
		Gatex = True
	if y > 0:
		Gatey = True
	if Gatex and Gatey:
		Horsey = [CellsDict[x-1, y-1], CellsDict[x-1, y], CellsDict[x-1, y+1], CellsDict[x, y], \
CellsDict[x, y], CellsDict[x, y+1], CellsDict[x, y-1], CellsDict[x+1, y-1], CellsDict[x+1, y], \
CellsDict[x+1, y+1]]
	elif Gatex and not Gatey:
		Horsey = [CellsDict[x-1, y], CellsDict[x-1, y+1], CellsDict[x, y], \
CellsDict[x, y], CellsDict[x, y+1], CellsDict[x+1, y], \
CellsDict[x+1, y+1]]
	elif Gatey and not Gatex:
		Horsey = [CellsDict[x, y], \
CellsDict[x, y], CellsDict[x, y+1], CellsDict[x, y-1], CellsDict[x+1, y-1], CellsDict[x+1, y], \
CellsDict[x+1, y+1]]
	for item in Horsey:
		if item.life == True:
			count += 1
		else:
			pass
	return count
	#Horesy because 'neigh'bors


# below this line is temp stuff, for testing.
brd = Board(25,25,fill="random")
# print brd.isLifeAt(1,1)
brd.printAsString()
print brd.CellsDict[1,1].Position_y
brd.advance()
brd.printAsString()
brd.advance()
brd.printAsString()
brd.advance()
brd.printAsString()
brd.advance()
brd.printAsString()
brd.advance()