#! /usr/bin/python

import pandas as pd
import numpy as np
import os
import time

import cell
import coordinate

start = time.time()

#Input the file name of the CSV
#inputCSVFile = 'beginner.csv'
inputCSVFile = 'testCorner.csv'

#Read the CSV file into a Dataframe
df = pd.read_csv(inputCSVFile, header=None)

totalMines=10
minesRemaining=totalMines

def decrementAdjCells(mineCell):
    #create a list of cells where the symbol is greater than or equal to 1
    numberCells=[]
    for key in mineCell.adjCells:
        if (mineCell.adjCells[key] != '?' and mineCell.adjCells[key] != '*' and mineCell.adjCells[key] != '0'):
            numberCells.append(key)
    
    #Loop through the list of numbered cells and decrement them on the dataframe
    for coordinates in numberCells:
        cellInt = int(df.at[coordinates.rowPos, coordinates.columnPos])
        cellInt = cellInt-1
        df.values[coordinates.rowPos, coordinates.columnPos] = str(cellInt)

#called when there is a bomb at the coordinates provided
def oneMine(mineRow, mineColumn):
    #place a bomb symbol in the entered coordinated
    df.values[mineRow, mineColumn]='*'

    #create a centerCell object at mine location if it is in a center cell
    if mineRow>0 and mineRow<(gridRows-1) and mineColumn>0 and mineColumn<(gridColumns-1):
        mineCell=cell.centerCell(mineRow, mineColumn, df)
        decrementAdjCells(mineCell)

    #Mine is in the top row, not the corners
    elif mineRow==0 and mineColumn>0 and mineColumn<(gridColumns-1):
        mineCell=cell.topEdgeCell(mineRow, mineColumn, df)
        decrementAdjCells(mineCell)
    #Mine is in the botton row, not the corners
    elif mineRow==(gridRows-1) and mineColumn>0 and mineColumn<(gridColumns-1):
        mineCell=cell.bottomEdgeCell(mineRow, mineColumn, df)
        decrementAdjCells(mineCell)
    #Mine is in the left column, not the corners
    elif mineColumn==0 and mineRow>0 and (mineRow<gridRows-1):
        mineCell=cell.leftEdgeCell(mineRow, mineColumn, df)
        decrementAdjCells(mineCell)
    #Mine is in the right column, not the corners
    elif mineColumn==(gridColumns-1) and mineRow>0 and (mineRow<gridRows-1):
        mineCell=cell.rightEdgeCell(mineRow, mineColumn, df)
        decrementAdjCells(mineCell)

    #Mine is in the top left corner
    elif mineRow==0 and mineColumn==0:
        mineCell=cell.topLeftCell(mineRow, mineColumn, df)
        decrementAdjCells(mineCell)
    #Top Right
    elif mineRow==0 and mineColumn==gridColumns-1:
        mineCell=cell.topLeftCell(mineRow, mineColumn, df)
        decrementAdjCells(mineCell)
    # Bottom Left
    elif mineRow==mineRow-1 and mineColumn==0:
        mineCell=cell.topLeftCell(mineRow, mineColumn, df)
        decrementAdjCells(mineCell)
    #Bottom Right
    elif mineRow==mineRow-1 and mineColumn==gridColumns-1:
        mineCell=cell.topLeftCell(mineRow, mineColumn, df)
        decrementAdjCells(mineCell)

def findMines(cell):
    #Given a cell, find the unknown cells that are the mines and decrement
    mineCells=[]
    
    for coordinate in cell.adjCells.keys():
        if (cell.adjCells[coordinate] == '?'):
            mineCells.append(coordinate)

    for coordinate in mineCells:
        oneMine(coordinate.rowPos, coordinate.columnPos)
    return mineCells

def check121Mine(cell):
    currRow = cell.currPos.rowPos
    currColumn = cell.currPos.columnPos
    
    topCellCoordinate = coordinate.coordinate(currRow-1,currColumn)
    bottomCellCoordinate = coordinate.coordinate(currRow-1,currColumn)
    leftCellCoordinate = coordinate.coordinate(currRow-1,currColumn)
    rightCellCoordinate = coordinate.coordinate(currRow-1,currColumn)
    

    if (cell.adjCells[])



gridRows = df.shape[0]
gridColumns = df.shape[1]

#Print the raw format of dataframe
for i in range(gridRows):#iterate over rows
    for j in range(gridColumns):#iterate over columns
        value = df.at[i,j]
        print(value, end="\t")
    print()

print('-------------------------------')

for rowIter in range(0, gridRows):
    for columnIter in range(0, gridColumns):
        value = df.at[rowIter, columnIter]
        if (value!='0' and value!='*' and value!='?'):
            if (rowIter==0 and columnIter==0):#Top Left Corner
                currCell=cell.topLeftCell(rowIter, columnIter,df)
            elif (rowIter==0 and columnIter==gridColumns-1):#Top Right
                currCell=cell.topRightCell(rowIter, columnIter,df)
            elif (rowIter==gridRows-1 and columnIter==0):#Bottom Left
                currCell=cell.bottomLeftCell(rowIter, columnIter,df)
            elif (rowIter==gridRows-1 and columnIter==gridColumns-1):#Bottom Right
                currCell=cell.bottomRightCell(rowIter, columnIter,df)

            elif (rowIter==0 and columnIter>0 and columnIter<gridColumns-1):#Top Edge
                currCell=cell.topEdgeCell(rowIter, columnIter,df)
            elif (rowIter==gridRows-1 and columnIter>0 and columnIter<gridColumns-1):#Bottom Edge
                currCell=cell.bottomEdgeCell(rowIter, columnIter,df)
            elif (rowIter>0 and rowIter<gridRows-1 and columnIter==0):#Left Edge
                currCell=cell.leftEdgeCell(rowIter, columnIter,df)
            elif (rowIter>0 and rowIter<gridRows-1 and columnIter==gridColumns-1):#Right Edge
                currCell=cell.rightEdgeCell(rowIter, columnIter,df)

            else:#Center Cell
                currCell=cell.centerCell(rowIter, columnIter,df)
            
            #If the value of the cell is equal to the number of adjacent unknown cells, then there are mines in the unknown cells    
            if (currCell.numUnknownAdjCells==int(value)):
                mineCoordinates=findMines(currCell)
                for i in range(int(value)):
                    minesRemaining=minesRemaining-1
           
            #If there is a 1-2-1 mine placement situation, check and assign mines accordingly
            if(int(value) == 2):
                check121Mine(currCell)
            

end = time.time()

print("The time elapsed is: ", (end-start) * 10**3, "ms")

print('-------------------------------')

#Print the raw format of dataframe
for i in range(gridRows):#iterate over rows
    for j in range(gridColumns):#iterate over columns
        value = df.at[i,j]
        print(value, end="\t")
    print()
