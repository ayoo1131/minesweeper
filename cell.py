

#Parent class to represent a cell on the board
class cell:
    def __init__(self, rowPos, columnPos):
        self.currPos = coordinate(rowPos, columnPos)
        self.cellSymbol=df.at[rowPos, columnPos]

        self.numUnknownAdjCells = 0
        for key in self.adjCells:
            if self.adjCells[key]=='?':
                self.numUnknownAdjCells=self.numUnknownAdjCells+1

#Child class to represent a center cell on the board
class centerCell(cell):
    def __init__(self, rowPos, columnPos):
        super().__init__(rowPos, columnPos)
        self.adjCells = {
                coordinate(rowPos-1, columnPos-1):df.at[rowPos-1, columnPos-1],
                coordinate(rowPos-1, columnPos):df.at[rowPos-1, columnPos],
                coordinate(rowPos-1, columnPos+1):df.at[rowPos-1, columnPos+1],
                coordinate(rowPos, columnPos-1):df.at[rowPos, columnPos-1],
                coordinate(rowPos, columnPos+1):df.at[rowPos, columnPos+1],
                coordinate(rowPos+1, columnPos-1):df.at[rowPos+1, columnPos-1],
                coordinate(rowPos+1, columnPos):df.at[rowPos+1, columnPos],
                coordinate(rowPos+1, columnPos+1):df.at[rowPos+1, columnPos+1],
                }

