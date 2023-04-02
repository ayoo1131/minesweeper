#! /usr/bin/python

import pandas as pd
import  numpy as np
import os
import time

start = time.time()

#Input the file name of the CSV
#inputCSVFile = 'beginner.csv'
inputCSVFile = 'testCorner.csv'

#Read the CSV file into a Dataframe
df = pd.read_csv(inputCSVFile, header=None)

#Create an object to represent a center cell
class centerCell:
    def __init__(self, rowPos, columnPos):
        self.rowPos = rowPos
        self.columnPos = columnPos
        

        self.cellSymbol=df.at[rowPos, columnPos]
        self.adjCells = {
                'Tl':df.at[rowPos-1, columnPos-1],
                'TC':df.at[rowPos-1,  columnPos],
                'TR':df.at[rowPos-1, columnPos+1],
                'CL':df.at[rowPos, columnPos-1],
                'CR':df.at[rowPos, columnPos+1],
                'BL':df.at[rowPos+1, columnPos-1],
                'BC':df.at[rowPos+1, columnPos],
                'BR':df.at[rowPos+1, columnPos+1]
                }

        self.numUnknownAdjCells = 0
        for key in self.adjCells:
            if self.adjCells[key]=='?':
                self.numUnknownAdjCells=self.numUnknownAdjCells+1


gridRows = df.shape[0]-1
gridColumns = df.shape[1] -1

for rowIter in range(1,gridRows-1):
    for columnIter in range(1, gridColumns-1):
        value = df.at[rowIter, columnIter]
        if value=='1':
            currCell = centerCell(rowIter, columnIter)
            print(currCell.adjCells)
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
