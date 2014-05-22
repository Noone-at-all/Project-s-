#!/usr/bin/env python2
import random
"""
Conway's Game of Life
http://en.wikipedia.org/wiki/Conway's_Game_of_Life#Rules
Rules: 
1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overcrowding.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""
CellsDict = {}
from random import randint

grid = []
for i in range(20):
	grid.append('0' * 20)
def DrawGrid(grid):
	for row in grid:
		print ''.join(row)
		
def MakeBoard(x, y):
	global boardx
	boardx = x
	global boardy
	boardy = y
	for item in range(x):
		for i in range(y):
			Rand = randint(1, 50)
			if Rand % 2 == 0:
				L = True
			else:
				L = False
			CellsDict[item, i] = Cell(item, i, L)

class Board(object):
	def __init__(self,x,y,fill="random"):
		# creates a board object that is x columns wide by y rows tall
		self.width = x
		self.height = y
		self.x = x
		self.y = y
		self.CellsDict = {}
		for row in range(self.x):
			for column in range(self.y):
				if fill == "random":
					self.CellsDict[row,column] = Cell( row, column, random.choice([True,False]) )
				elif fill == "blank":
					self.CellsDict[row,column] = Cell( row, column, False )
				elif fill == "Full":
					self.CellsDict[row,column] = Cell( row, column, True )
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
	def WillBeAliveNextRound(self):
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

def CountLivingNeighbors(x, y):
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

def PresentBoard():
	YList = range(boardy)
	XList = range(boardx)
	CurrentY = YList[len(YList)-1]
	CurrentX = XList[0]
	while CurrentY >= 0:
		while CurrentX <= len(XList)-1:
			print CellsDict[CurrentX, CurrentY].CoLi,
			CurrentX += 1
		CurrentY -= 1
		CurrentX = XList[0]
		print ''
brd = Board(5,5)
print brd.CellsDict