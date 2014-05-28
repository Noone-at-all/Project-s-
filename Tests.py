#!/usr/bin/env python2
import random
import pygame, sys, os 
from pygame.locals import *
#############################
### Conway's Game of Life ###
#############################
# http://en.wikipedia.org/wiki/Conway's_Game_of_Life#Rules
# Rules: 
# 1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
# 2. Any live cell with two or three live neighbours lives on to the next generation.
# 3. Any live cell with more than three live neighbours dies, as if by overcrowding.
# 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
pygame.init()
ScreenSize = (800,600)
screen = pygame.display.set_mode(ScreenSize)
BgColor = (0,0,0)
screen.fill(BgColor)
clock = pygame.time.Clock()
pygame.display.set_caption("Conway's Game of Life")

'''
def Board():
	for x in range(0,800,10):
			for y in range(0,600,10):
				CellsDict[x,y] = Cell(x, y, random.choice([True,False]))
	#print CellsDict

def isLifeAt(x,y):
		return CellsDict[x,y].life

def CountLivingNeighbors(x,y):
	neighbors = 0
	for column in xrange(x-10,x+20): #10s because of dot size
		for row in xrange(y-10,y+20):
			if not (column,row) == (x,y): # so we don't count the given cell
				# tries to do all 8 bordering cells, and soft-fails if a cell does not exist
				# (which could happen if the given coordinates are on the border)
				try:
					if isLifeAt(column,row):
						neighbors += 1
				except:
					pass
	return neighbors

def WillCellBeAliveNextRound(x, y):
	# determine whether the cell at x, y will be alive next round
	# this code is modified from dav's original function elsewhere
	LivingNeighbors = CountLivingNeighbors(x,y)
	if LivingNeighbors < 2:
		return False
	if LivingNeighbors == 3:
		return True
	if LivingNeighbors > 3:
		return False
	if LivingNeighbors == 2:
		return isLifeAt(x,y)

def DrawLife(): #Draws a dot onto the screen based on the life values found in CellsDict
	for cell in CellsDict:
		cellX = CellsDict.PositionX
		cellY = CellsDict.PositionY
		cellLife = WillCellBeAliveNextRound(cellX,cellY)
		if cellLife == True:
			dot = pygame.Rect(cellX,cellY,10,10) #pygame draws a 10x10 rectangle at cellx, celly 
			screen.fill((255,255,255),dot) #pygame fills the rectangle with the color white
			pygame.display.update() #updates display
		else:
			pass

'''
class Board(object):
	"""docstring for Board"""
	def __init__(self):
		self.CellsDict = {}
		#creates a dictionary of x,y cords spanning the entire 800x600 screen
		#that are spaced by 10 for the size of the dot
		for x in range(0,800,10):
			for y in range(0,600,10):
				self.CellsDict[x,y] = Cell(x, y, random.choice([True,False]))
		#print CellsDict

	def isLifeAt(self,x,y):
		return self.CellsDict[x,y].life

	def CountLivingNeighbors(self,x,y):
		neighbors = 0
		for column in xrange(x-10,x+20): #10s because of dot size
			for row in xrange(y-10,y+20):
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

	def DrawLife(self): #Draws a dot onto the screen based on the life values found in CellsDict
		for cell in CellsDict:
			cellX = self.CellsDict.PositionX
			cellY = self.CellsDict.PositionY
			cellLife = self.WillCellBeAliveNextRound(cellX,cellY)
			if cellLife == True:
				dot = pygame.Rect(cellX,cellY,10,10) #pygame draws a 10x10 rectangle at cellx, celly 
				screen.fill((255,255,255),dot) #pygame fills the rectangle with the color white
				pygame.display.update() #updates display
			else:
				pass

class Cell(object):
	"""docstring for Cell"""
	def __init__(self, x,y,life):
		self.PositionX = x
		self.PositionY = y
		self.life = life
	def __repr__(self):
		return "{life}, and at ({x},{y})".format(life=str(self.life), x=str(self.PositionX), y=str(self.PositionY))

Board()
Board.DrawLife()

#just drawing a dot to see if everything works..... TEMP.
'''
sqr = pygame.Rect(10,10,10,10)
screen.fill((255,255,255),sqr)
pygame.display.update()
'''
