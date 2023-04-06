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

#Loop through the center cells
for rowIter in range(1,gridRows-1):
    for columnIter in range(1, gridColumns-1):
        value = df.at[rowIter, columnIter]
        #If there is a bomb in corner edge
        if value=='1':
            print("yo")
            currCell = cell.centerCell(rowIter, columnIter, df)
            
            if (currCell.numUnknownAdjCells==1):
                print ('yes')
                #Find the cell that is the unknown cell that is the bomb
                bomb = list(cell.currCell.adjCells.keys())[list(cell.currCell.adjCells.values()).index('?')]
                cornerBomb(bomb.rowPos, bomb.columnPos)            

        print(value, end="\t")
    print()

end = time.time()

print("The time elapsed is: ", (end-start) * 10**3, "ms")

print('-------------------------------')

#Print the raw format of dataframe
for i in range(gridRows):#iterate over rows
    for j in range(gridColumns):#iterate over columns
        value = df.at[i,j]
        print(value, end="\t")
    print()
