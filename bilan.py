import pandas as pd
import difflib
from similarityRatio import similarityRatio

def bilan(config, results, paramA, avgSprmnIndex, df, biclusters):
    """Stores biclustering results inside .csv file in an organised fashion
       And calculates similarity index ratio between each result"""

    file = open(results, "r")
    lines = file.readlines()

    map = dict()
    asrTotal = 0
    numLines = 0
    biclSizeList = []
    localBiclusters = []  #local list which stores biclusters of a process

    #Start parsing from line 2 since lines above contain redundant information
    for i in range(2,len(lines)):

        numLines += 1
        biclusterSize = 0

        #Declare lists to store parsed data
        conditions, evaluations, li, bicluster = [], [], [], []

        #Parse line by line
        line = lines[i]

        #Omit row ID "Genes"
        result = line[7:len(line)-1]

        map["Index"] = avgSprmnIndex
        map["Parameter"] = paramA

        #Start reading rows and columns of data matrix or resp. samples and conditions
        trimmedLine = ''
        for c in result:
            if c.isalnum() or c == ".":
                trimmedLine += c
            else:
                li.append(trimmedLine)
                trimmedLine = ''
        li.append(trimmedLine)

        while ('' in li):
            li.remove('')
    
        for i in range(0, li.index('Conditions')):
            evaluations.append(li[i])

        for j in range(li.index('Conditions')+1, li.index('ASR')):
            conditions.append(li[j])

        #Parse ASR index and calculate sum of bicluster's indices
        asr = float(result[result.index(':')+1:len(result)])
        asrTotal += asr

        #Converts entries of data matrix into tuples
        for i in range(0, len(conditions)):
            for j in range(0, len(evaluations)):
                biclusterSize += 1
                entry = (conditions[i],evaluations[j])
                bicluster.append(entry)
        
        biclSizeList.append(biclusterSize)
        
        #Save biclusters inside data structures
        biclusters.append(bicluster)
        localBiclusters.append(bicluster)

        column = "["
        for k in range(len(conditions)-1):
            column += conditions[k] + ","
        column += conditions[len(conditions)-1] + "]"

        map["Conditions " + column] = "ASR:{} {}".format(asr, evaluations)

        #---------------------------------------------------------------------------------------------

    #Calculates max overlap ratio of biclusters
    maxRatio = max(similarityRatio(localBiclusters))
    
    file.close()

    """Return new object of type Dataframe which contains biclustering results
       Return number of biclusters
       Return mean value of ASR
       inside a tuple"""
    return (df.append(map, ignore_index=True), numLines, asrTotal / numLines, biclSizeList, maxRatio)