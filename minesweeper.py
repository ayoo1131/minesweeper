#! /usr/bin/python

import pandas as pd
import  numpy as np
import os
import time

start = time.time()

#Input the file name of the CSV
inputCSVFile = 'beginner.csv'
#inputCSVFile = 'testCorner.csv'

#Read the CSV file into a Dataframe
df = pd.read_csv(inputCSVFile, header=None)

#Create an object to represent a coordinate on the board
class coordinate:
    def __init__(self, rowPos, columnPos):
        self.columnPos = columnPos
        self.rowPos = rowPos


#Create an object to represent a center cell
class centerCell:
    def __init__(self, rowPos, columnPos):
        self.currPos = coordinate(rowPos, columnPos)
        self.cellSymbol=df.at[rowPos, columnPos]
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

        self.numUnknownAdjCells = 0
        for key in self.adjCells:
            if self.adjCells[key]=='?':
                self.numUnknownAdjCells=self.numUnknownAdjCells+1
    
#called when there is a bomb at the coordinates provided
def cornerBomb(bombRow, bombColumn):
    #place a bomb symbol in the entered coordinated
    df.values[bombRow, bombColumn]='*'

    #create a centerCell object at bomb location if it is not on the edge of the board
    if (bombRow>0 and bombRow<gridRows-1 and bombColumn>0 and bombColumn<gridColumns-1):
        bombCell=centerCell(bombRow,bombColumn)

        #create a list of cells where the symbol is greater than 1
        numberCells=[]
        for key in bombCell.adjCells:
            if (bombCell.adjCells[key] != '?' and bombCell.adjCells[key] != '*' and bombCell.adjCells[key] != '0'):
                numberCells.append(key)
                      
        #Loop through the list of numbered cells and decrement them on the dataframe
        for coordinates in numberCells:
            cellInt = int(df.at[coordinates.rowPos, coordinates.columnPos])
            cellInt = cellInt-1
            df.values[coordinates.rowPos, coordinates.columnPos] = str(cellInt)
                       
gridRows = df.shape[0]
gridColumns = df.shape[1]

#Print the raw format of dataframe
for i in range(gridRows):#iterate over rows
    for j in range(gridColumns):#iterate over columns
        value = df.at[i,j]
        print(value, end="\t")
    print()

print('-------------------------------')

for rowIter in range(1,gridRows-1):
    for columnIter in range(1, gridColumns-1):
        value = df.at[rowIter, columnIter]
        if value=='1':
            currCell = centerCell(rowIter, columnIter)
            if (currCell.numUnknownAdjCells==1):
                bomb = list(currCell.adjCells.keys())[list(currCell.adjCells.values()).index('?')]
                #print("("+str(bomb.x)+", "+str(bomb.y)+")")
                #df.values[bomb.rowPos, bomb.columnPos] = '*'
                cornerBomb(bomb.rowPos, bomb.columnPos)            

        print(value, end="\t")
    print()

end = time.time()

print("The time elapsed is: ", (end-start) * 10**3, "ms")

#Print the raw format of dataframe
for i in range(gridRows):#iterate over rows
    for j in range(gridColumns):#iterate over columns
        value = df.at[i,j]
        print(value, end="\t")
    print()
