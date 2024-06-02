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
        self._grid