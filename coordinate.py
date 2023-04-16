#Create an object to represent a coordinate on the board
class coordinate:
    def __init__(self, rowPos, columnPos):
        self.columnPos = columnPos
        self.rowPos = rowPos

    def __hash__(self):
        return hash((self.rowPos, self.columnPos))

    def __eq__(self, other):
        return (self.rowPos, self.columnPos) ==(other.rowPos, other.columnPos)
