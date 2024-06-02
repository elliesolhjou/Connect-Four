import enum

class GridPosition(enum.Enum):
    EMPTY = 0
    YELLOW = 1
    RED = 2

# Grid class to maintain the state of the 2-D board
class Grid:
    def __init__(self, rows, cols):
        # "_" defines for internal use and encapsulation
        self._rows = rows
        self._cols = cols
        self._grid = None
        self.initGrid()

    def initGrid(self):
        # create 2D grid (list of lists)
        self._grid = [[GridPosition.EMPTY for i in range(self._cols)]for i in range(self._rows)]