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

#Create an object to represent center cells
class centerCell:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
        self.cellSymbol=df.at[x,y]
        self.adjCells = {'TL':df.at[x-1, y-1],
                'TC':df.at[x, y-1],
                'TR':df.at[x+1, y-1],
                'CL':df.at[x-1,y],
                'CR':df.at[x+1,y],
                'BL':df.at[x-1,y+1],
                'BC':df.at[x,y+1],
                'BR':df.at[x+1,y+1]}
    
        self.numUnknownAdjCells = 0
        for key in self.adjCells:
            if self.adjCells[key]=='?':
                self.numUnknownAdjCells=self.numUnknownAdjCells+1


gridRows = df.shape[0]-1
gridColumns = df.shape[1] -1

for x in range(1,gridRows-1):
    for y in range(1, gridColumns-1):
        value = df.at[x,y]
        if value=='1':
            currCell = centerCell(x,y)
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
