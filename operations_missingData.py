import sys
import random
import numpy as np
import pandas as pd

running = True

#tfile = open('test.txt', 'a')
#tfile.write(df.to_string())
#tfile.close()

#Iterates through a column, finds the missing data and assigns a value between min and max to it
def assignMin_Max(df):
    for index, row in df.iterrows():
        min = df.iloc[:,index+1].dropna().min()
        max = df.iloc[:,[index+1]].dropna().max()
        if df.iloc[:,index+1].dtype == np.float:
            x = random.uniform(min,max)
            df.iloc[:,[index+1]] = df.iloc[:,[index+1]].fillna(x)

        if index == len(df.columns)-2:
            break
    newDf = input('Enter the name of the file you would like to save your changes to: ')
    file = open(newDf, 'w')
    file.close()
    df.to_csv(newDf)


#Iterates through a column, finds the missing data and assigns a neutral value to it
def assignNeutralValue(df):
    for index, row in df.iterrows():
        df.iloc[:,[index+1]] = df.iloc[:,[index+1]].fillna(0)
        
        if index == len(df.columns)-2:
            break
    newDf = input('Enter the name of the file you would like to save your changes to: ')
    file = open(newDf, 'w')
    file.close()
    df.to_csv(newDf, index = False)


#Finds a column's average value and assigns every NaN to it
def averageValue(df):
    average = 0
    for index, row in df.iterrows():
        average = df.iloc[:,[index+1]].mean(skipna = True)
        print(index, average)
        df.iloc[:,[index+1]] = df.iloc[:,[index+1]].fillna(average)

        if index == len(df.columns)-2:
            break 
    newDf = input('Enter the name of the file you would like to save your changes to: ')
    file = open(newDf, 'w')
    file.close()
    df.to_csv(newDf, index = False)
    

#Finds String values and replaces them with 0
def labelEncoding(df):
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
    newDf = input('Enter the name of the file you would like to save your changes to: ')
    file = open(newDf, 'w')
    file.close()
    df.to_csv(newDf)

while running:  
    print('Enter the name of the file: ')
    file = input()
    df = pd.read_csv(file, engine = 'python')
    method = input('Choose the method with which you would like to replace the non values: A B C D   ')

    if method == 'A':
        averageValue(df)
    if method == 'B':
       assignMin_Max(df)
    if method == 'C':
       assignNeutralValue(df)
    if method == 'D':
       labelEncoding(df)

    running = input()
    