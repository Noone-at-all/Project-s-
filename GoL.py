"""
Conway's Game of Life
http://en.wikipedia.org/wiki/Conway's_Game_of_Life#Rules
Rules: 
Any live cell with fewer than two live neighbours dies, as if caused by under-population.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overcrowding.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""
class Game(object):
	"""docstring for Game"""
	def __init__(self, arg):
		super(Game, self).__init__()
		self.arg = arg

class Cell(object):
  	def __init__(self, position):
        self.position = position 
	class LivingCell(Cell):
    	IsAlive = True
    	def __init__(self, position):
        	self.position = position
        	self.IsAlive = IsAlive
	class DeadCell(Cell)
    	IsAlive = False
    	def __init__(self, position):
        	self.position = position
        	self.IsAlive = IsAlive

