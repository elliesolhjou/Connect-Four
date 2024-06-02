import enum

class GridPosition(enum.Enum):
    EMPTY = 0
    YELLOW = 1
    RED = 2

# Grid class to maintain the state of the 2-D board
# this class helps us to see if a cell is available or not grid[row][col] ==1
class Grid:
    # initialize
    def __init__(self, rows, cols):
        # "_" defines for internal use and encapsulation
        self._rows = rows
        self._cols = cols
        self._grid = None
        self.initGrid()

    # methods:
    # create 2D grid (list of lists)
    def initGrid(self):
        self._grid = [[GridPosition.EMPTY for i in range(self._cols)]for i in range(self._rows)]

    # access the grid
    def getGrid(self):
        return self._grid
    
    # access the grid sizes
    def getColumnsCount(self):
        return self._cols
    
    # access the grid sizes
    def getRowsCount(self):
        return self._rows
    
    # place tokens -> asks about columns bc drop token takes all the way 
    # down to the available cell
    def placePieces(self, column, piece):
        if column <0 or column >= self._cols:
            raise ValueError("Selected Column Doesn't Exist")
        if piece == GridPosition.EMPTY:
            raise ValueError("Invalid token, Please pick a yellow or red token")
        for row in range(self._rows-1, -1, -1):
            if self._grid[row][column] == GridPosition.EMPTY:
                self._grid[row][column] = piece
                return row
            
    # check win status of players
    # connectN likely the number of consecutive pieces 
    # needed to achieve a win in a game
    def checkWin(self, connectN, row, col, piece):
        count = 0
        # Check horizontal connections
        for c in range(self._cols):
            if self._grid[row][c] == piece:
                count+=1
            else:
                count = 0
            if count == connectN:
                return True
        # Check vertical connections
        for r in range(self._rows):
            if self._grid[r][col] == piece:
                count+=1

            else:
                count = 0
            if count == connectN:
                return True
            
        # check diagonal connections
        count = 0
        for r in range (self._rows):
            # get col position of diagonal
            c = row+col-r
            if c >= 0 and c < self._cols and self._grid[r][c] == piece:
                count+=1
            else:
                count = 0
            if count == connectN:
                return True
            
        # check anti-diagonal connections
        count = 0
        for r in range(self._rows):
            c = col - row + r
            if c >=0 and c < self._cols and self._grid[r][c] == piece:
                count+=1
            else:
                count = 0
            if count == connectN:
                return True
        
        return False


# encapsulate the player's information, 
# more importantly the player's piece color

class Player:
    # initialize
    def __init__ (self, name, pieceColor):
        self._name = name
        self._pieceColor = pieceColor
    
    # methods for players
    def getName(self):
        return self._name
    def getPieceColor(self):
        return self._pieceColor
