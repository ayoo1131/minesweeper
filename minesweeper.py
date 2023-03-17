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

gridRows = df.shape[0]-1
gridColumns = df.shape[1] -1

#Check each corner of the grid to see if it is a bomb
topLeft = df.at[0, 0]
topRight = df.at[0, gridColumns]
bottomLeft = df.at[gridRows, 0]
bottomRight = df.at[gridRows, gridColumns]
if (topLeft=="1" or topRight=="1" or bottomLeft=="1" or bottomRight=="1"):

    #If there is a 1 in the top left corner
    if(topLeft=="1"): 
        if(df.at[0, 1]=='?' or df.at[1, 1]=='?' or df.at[1, 0]=='?'):
            numQuestion=0
            if (df.at[0, 1]=='?'):
                numQuestion+=1
                
            if (df.at[1, 1]=='?'):
                numQuestion+=1
                
            if (df.at[1, 0]=='?'):
                numQuestion+=1
            
            if(numQuestion==1):
                print("There is a bomb at (1,1)")
                df.values[0,0]='0'
                df.values[0,1]='0'
                df.values[1,0]='0'
                df.values[1,1]='*'
    
    #If there is a 1 in the top left corner 
    if (topRight=="1"):
        if(df.at[0,gridColumns-1] == '?' or df.at[1,gridColumns-1] == '?' or df.at[1, gridColumns]=='?'):
            numQuestion=0
            if (df.at[0,gridColumns-1] =='?'):
                numQuestion+=1
                
            if (df.at[1,gridColumns-1] =='?'):
                numQuestion+=1
                
            if (df.at[1, gridColumns]=='?'):
                numQuestion+=1
                
            if(numQuestion==1):
                print("There is a bomb at (1,7)")
                df.values[0,gridColumns]='0'
                df.values[0,gridColumns-1]='0'
                df.values[1,gridColumns]='0'
                df.values[1,gridColumns-1]='*'   
     
    #If there is a 1 in the bottom left corner 
    if(bottomLeft=="1"):
        if(df.at[gridRows-1, 0] == '?' or df.at[gridRows-1, 1] == '?' or df.at[gridRows, 1] =='?'):
            numQuestion=0
            if (df.at[gridRows-1, 0] =='?'):
                numQuestion+=1
                
            if (df.at[gridRows-1, 1] =='?'):
                numQuestion+=1
                
            if (df.at[gridRows, 1] =='?'):
                numQuestion+=1
                
            if(numQuestion==1):
                print("There is a bomb at (7,1)")
                df.values[gridRows-1, 0]='0'
                df.values[gridRows, 0]='0'
                df.values[gridRows, 1]='0'
                df.values[gridRows-1, 1]='*'   
        
    #If there is a 1 in the bottom right corner     
    if(bottomRight=="1"):
        if(df.at[gridRows-1,gridColumns] == '?' or df.at[gridRows-1, gridColumns-1] == '?' or df.at[gridRows, gridColumns-1]=='?'):
            numQuestion=0
            if (df.at[gridRows-1,gridColumns] =='?'):
                numQuestion+=1
                
            if (df.at[gridRows-1, gridColumns-1] =='?'):
                numQuestion+=1
                
            if (df.at[gridRows, gridColumns-1] =='?'):
                numQuestion+=1
                
            if(numQuestion==1):
                print("There is a bomb at (7,7)")
                df.values[gridRows-1, gridColumns]='0'
                df.values[gridRows, gridColumns]='0'
                df.values[gridRows, gridColumns-1]='0'
                df.values[gridRows-1, gridColumns-1]='*'   
        
#Check the edge cells of the minesweeper board

#Check the top edge
for x in range (1, numColumns):
    if (df.at[0,x] == '1'):
        numQuestions=0
        if df.at[0,x-1] == ''



end = time.time()

print("The time elapsed is: ", (end-start) * 10**3, "ms")

#Print the 
for i in range(gridRows):#iterate over rows
    for j in range(gridColumns):#iterate over columns
        value = df.at[i,j]
        print(value, end="\t")
    print()