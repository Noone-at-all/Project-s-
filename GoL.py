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
CellsDict = {}
from random import randint
def MakeBoard(x, y):
    for item in range(x):
        for i in range(y):
            Rand = randint(1, 50)
            if Rand % 2 == 0:
                L = True
            else:
                L = False
            CellsDict[item, i] = Cell(item, i, L)
class Cell(object):
    def __init__(self, x, y, life): #Life is a bool value
        self.positionx = x
        self.positiony = y
        self.life = life
    def __repr__(self):
        return '(%s, %s)' % (str(self.positionx), str(self.positiony))
    def isalive(self):
        pass #Will soon be given substance.
#A template cell.
def CountLN(x, y):
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
def ShouldBeLiving(x, y):
    CPL = [x, y]
    MC = CellsDict[x, y]
    LN = CountLN(x, y)
    if LN < 2:
        return False
    if LN == 3:
        return True
    if LN > 3:
        return False
    if LN == 2:
        return MC.life
        #Returns True if the cell should be alive, and False if it shouldn't,
class LivingCell(Cell):#Does not need to exist
    def __repr__(self):
        return '(%s, %s), %s' % (str(self.positionx), str(self.positiony), str(self.life))
#Living cells, soon to be improved.
class DeadCell(Cell):#See LivingCell
    def __repr__(self):
        return '(%s, %s), %s' % (str(self.positionx), str(self.positiony), str(self.life))
#Dead cells, soon to be living.
