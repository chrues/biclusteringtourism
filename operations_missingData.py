import sys
import random
import numpy as np
import pandas as pd

#tfile = open('test.txt', 'a')
#tfile.write(df.to_string())
#tfile.close()

#Iterates through a column, finds the missing data and assigns a value between min and max to it
def assignRandomValueBetweenMinMax(df):
    for index, row in df.iterrows():
        min = df.iloc[:,index+1].dropna().min()
        max = df.iloc[:,[index+1]].dropna().max()
        if df.iloc[:,index+1].dtype == np.float:
            x = random.uniform(min,max)
            df.iloc[:,[index+1]] = df.iloc[:,[index+1]].fillna(x)

        if index == len(df.columns)-2:
            break
    newDf = input(print('Enter the name of the file you would like to save your changes to: '))
    df.to_csv(newDf)


#Iterates through a column, finds the missing data and assigns a random neutral value to it
def assignNeutralValue(df):
    for index, row in df.iterrows():
        df.iloc[:,[index+1]] = df.iloc[:,[index+1]].fillna(0)
        
        if index == len(df.columns)-2:
            break
    newDf = input(print('Enter the name of the file you would like to save your changes to: '))
    df.to_csv(newDf)


#Finds a column's average value and assigns every NaN to it
def averageValue(df):
    average = 0
    for index, row in df.iterrows():
        average = df.iloc[:,[index+1]].mean(skipna = True)
        print(index, average)
        df.iloc[:,[index+1]] = df.iloc[:,[index+1]].fillna(average)

        if index == len(df.columns)-2:
            break 
    newDf = input(print('Enter the name of the file you would like to save your changes to: '))
    df.to_csv(newDf)
    

#Finds String values and replaces them with 0
def removeElement(df):
    headers = list(df.columns)
    for index, row in df.iterrows():
        header = headers[index+1]
        if (not header == 'USER') and (df.iloc[:,index+1].dtype == np.object):
            df[header] = -1
        
        if index == len(df.columns)-2:
            break
    newDf = input(print('Enter the name of the file you would like to save your changes to: '))
    df.to_csv(newDf)
    

file = input(print('Enter the name of the file: '))
df = pd.read_csv(file, engine = 'python')
method = input(print('Choose the method with which you would like to replace the non values: A B C D'))

if method == 'A':
    averageValue(df)
if method == 'B':
    assignMin_Max(df)
if method == 'C':
    assignNeutralValue(df)
if method == 'D':
    removeElement(df)
    