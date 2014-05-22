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
class Game(object):
	"""docstring for Game"""
	def __init__(self, arg):
		super(Game, self).__init__()
		self.arg = arg
CellsDict = {}
def MakeBoard(x, y):
    for item in range(x):
        for i in range(y):
            File.write('Cell(%s, %s) = Cell(%s, %s)' % (str(item), str(i), int(item), int(i)))
            File.write('\n')
            CellsDict[item, i] = Cell(item, i)
class Cell(object):
    def __init__(self, x, y):
        self.positionx = x
        self.positiony = y
    def CheckLife(self):
        self,life = 'You\'re checking, and I\'m still between dead and alive.'
    def __repr__(self):
        return '(%s, %s)' % (str(self.positionx), str(self.positiony))
    def isalive(self):
        pass
#A template cell.
class LivingCell(Cell):
    def __repr__(self):
        return '(%s, %s), %s' % (str(self.positionx), str(self.positiony), str(self.life))
#Living cells, soon to be improved.
class DeadCell(Cell):
    def __repr__(self):
        return '(%s, %s), %s' % (str(self.positionx), str(self.positiony), str(self.life))
#Dead cells, soon to be living.
