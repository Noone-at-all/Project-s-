"""
Conway's Game of Life
http://en.wikipedia.org/wiki/Conway's_Game_of_Life#Rules
Rules: 
Any live cell with fewer than two live neighbours dies, as if caused by under-population.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overcrowding.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""
File = open('CellList.txt', 'w')
def MakeBoard(x, y):
#Makes the cells we need for the game.
    for item in range(x):
        for i in range(y):
            File.write('Cell(%s, %s) = Cell(%s, %s)' % (str(item), str(i), int(item), int(i)))
            File.write('\n')
class Game(object):
	"""docstring for Game"""
	def __init__(self, arg):
		super(Game, self).__init__()
		self.arg = arg

class Cell(object):
    def __init__(self, position):
        self.position = position
    def isalive(self):
    	
class LivingCell(Cell):
    def __init__(self, position):
        self.position = position
class DeadCell(Cell)
    def __init__(self, position):
        self.position = position
