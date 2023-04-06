import coordinate

#Parent class to represent a cell on the board
class cell:
    def __init__(self, rowPos, columnPos, df):
        self.currPos = coordinate.coordinate(rowPos, columnPos)
        self.cellSymbol=df.at[rowPos, columnPos]
        self.adjCells = {}
        self.numUnknownAdjCells = 0
        
    def calculateNumUnknownAdjCells(self):
        unknownCells=0
        for key in self.adjCells:
            if self.adjCells[key]=='?':
                unknownCells=unknownCells+1

        return unknownCells

#Child class to represent a center cell on the board
class centerCell(cell):
    def __init__(self, rowPos, columnPos,df):
        super().__init__(rowPos, columnPos, df)
        self.adjCells = {
                coordinate.coordinate(rowPos-1, columnPos-1):df.at[rowPos-1, columnPos-1],
                coordinate.coordinate(rowPos-1, columnPos):df.at[rowPos-1, columnPos],
                coordinate.coordinate(rowPos-1, columnPos+1):df.at[rowPos-1, columnPos+1],
                coordinate.coordinate(rowPos, columnPos-1):df.at[rowPos, columnPos-1],
                coordinate.coordinate(rowPos, columnPos+1):df.at[rowPos, columnPos+1],
                coordinate.coordinate(rowPos+1, columnPos-1):df.at[rowPos+1, columnPos-1],
                coordinate.coordinate(rowPos+1, columnPos):df.at[rowPos+1, columnPos],
                coordinate.coordinate(rowPos+1, columnPos+1):df.at[rowPos+1, columnPos+1],
                }

        self.numUnknownAdjCells = self.calculateNumUnknownAdjCells()

