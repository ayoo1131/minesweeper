#! /usr/bin/python

import pandas as pd
import numpy as np
import os
import time

import cell
import coordinate

start = time.time()

#Input the file name of the CSV
inputCSVFile = 'beginner.csv'
#inputCSVFile = 'testCorner.csv'

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

    #create a centerCell object at bomb location if it is not on the edge of the board
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
        
    #Mine is in the left column, not the coernes
    elif mineColumn==0 and mineRow>0 and (mineRow<gridRows-1):
        mineCell=cell.leftEdgeCell(mineRow, mineColumn, df)
        decrementAdjCells(mineCell)
    
    #Mine is in the right column, not the noerners
    elif mineColumn==(gridColumns-1) and mineRow>0 and (mineRow<gridRows-1):
        mineCell=cell.rightEdgeCell(mineRow, mineColumn, df)
        decrementAdjCells(mineCell)

def findMines(cell):
    #Given a cell, find the unknown cells that are the mines and decrement
    #bomb = list(currCell.adjCells.keys())[list(currCell.adjCells.values()).index('?')]
    mineCells=[]
    
    for coordinate in cell.adjCells.keys():
        if (cell.adjCells[coordinate] == '?'):
            mineCells.append(coordinate)

    for coordinate in mineCells:
        oneMine(coordinate.rowPos, coordinate.columnPos)


    #for i in range(len(cell.adjCells)):
    #    cell.adjCells.get(i)
        
    #print(bomb)
    #oneMine(bomb.rowPos, bomb.columnPos)


gridRows = df.shape[0]
gridColumns = df.shape[1]

#Print the raw format of dataframe
for i in range(gridRows):#iterate over rows
    for j in range(gridColumns):#iterate over columns
        value = df.at[i,j]
        print(value, end="\t")
    print()

print('-------------------------------')

#Loop through the center cells
for rowIter in range(1, gridRows-1):
    for columnIter in range(1, gridColumns-1):
        value = df.at[rowIter, columnIter]
        if (value!='0' and value!='*' and value!='?'):
            currCell = cell.centerCell(rowIter, columnIter, df)
            if (currCell.numUnknownAdjCells==int(value)):
                findMines(currCell)
                for i in range(int(value)):
                    minesRemaining=minesRemaining-1
                #Find the unknown cells that are the mines
        print(value, end="\t")
    print("There are "+str(minesRemaining)+" mines left")

end = time.time()

print("The time elapsed is: ", (end-start) * 10**3, "ms")

print('-------------------------------')

#Print the raw format of dataframe
for i in range(gridRows):#iterate over rows
    for j in range(gridColumns):#iterate over columns
        value = df.at[i,j]
        print(value, end="\t")
    print()
