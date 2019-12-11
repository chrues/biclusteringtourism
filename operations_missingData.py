import sys
import random
import numpy as np
import pandas as pd

#running = True

def saveChanges(df):
    newDf = input('Enter the name of the file you would like to save your changes to: ')
    file = open(newDf, 'w')
    file.close()
    df.to_csv(newDf, index = False)

def assignMin_Max(df):
    """Iterates through a column, finds the missing data and assigns a value between min and max to it"""

    for index, row in df.iterrows():
        min = df.iloc[:,index+1].dropna().min()
        max = df.iloc[:,[index+1]].dropna().max()
        if df.iloc[:,index+1].dtype == np.float:
            x = random.uniform(min,max)
            df.iloc[:,[index+1]] = df.iloc[:,[index+1]].fillna(x)

        if index == len(df.columns)-2:
            break
    saveChanges(df)

def assignNeutralValue(df):
    """Iterates through a column, finds the missing data and assigns a neutral value to it"""

    for index, row in df.iterrows():
        df.iloc[:,[index+1]] = df.iloc[:,[index+1]].fillna(0)
        
        if index == len(df.columns)-2:
            break
    saveChanges(df)

def averageValue(df):
    """Finds a column's mean value and assigns it to every instance of type NaN"""

    average = 0
    for index, row in df.iterrows():
        average = df.iloc[:,[index+1]].mean(skipna = True)
        print(index, average)
        df.iloc[:,[index+1]] = df.iloc[:,[index+1]].fillna(average)

        if index == len(df.columns)-2:
            break 
    saveChanges(df)
    
def labelEncoding(df):
    """Finds String values and replaces them with categorical labels 
       Strings sharing the same value will have an identical label assigned to them"""

    headers = list(df.columns)
    for i in range(0,len(df.columns)): 
        if df.iloc[:,i].dtype == np.object:
            df[df.columns[i]] = df[df.columns[i]].astype('category')
            df[df.columns[i]] = df[df.columns[i]].cat.codes
    
    #for index, row in df.iterrows():
     #   header = headers[index+1]
        #if (not header == 'USER') and (df.iloc[:,index+1].dtype == np.object):
         #   df[header] = -1
        
        #if index == len(df.columns)-2:
            #break
    saveChanges(df)