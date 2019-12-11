import subprocess
import shutil
import pandas as pd
import time
from bilan import bilan
import difflib
from similarityRatio import similarityRatio

parametersA = [2, 4, 6]

def jarWrapper(exec, txt, config, start_time):
    """Method to call the bi-clustering executable from within Python using the module 'subprocess'
       It accesses our applications by creating new process(es)"""

    #Creates an empty dataframe, hence index=[]
    df = pd.DataFrame(index=[])

    files, biclusters = [], []
    inputFile = txt + '.txt'

    for i in range(0,len(parametersA)):
        #To compute the interval [-0.6, 0.6]
        for j in range(1, 7):
            #Corresponds to the minimum number of columns to be evaluated
            paramA = parametersA[i]

            #Correlation index between rows and columns
            avgSprmnIndex = -0.6 + 0.2 * j

            #Create new output file to store biclusters
            outputFile = "{}_results-{}-{}_{}.txt".format(txt, exec, paramA, avgSprmnIndex)
            file = open(outputFile, 'w')
            print("Writing to {}...".format(outputFile))

            #Executes the algorithm on file
            subprocess.call([exec, inputFile, str(paramA), str(avgSprmnIndex), outputFile], shell=True)

            file.close()
            files.append(outputFile)

            ###
            df, numBiclusters, asrMean, biclSizeList, maxRatio = bilan(config, outputFile, paramA, avgSprmnIndex, df, biclusters)
            print("Setup [{}, {}]".format(paramA, avgSprmnIndex))
            print("This process produces {} biclusters".format(numBiclusters))
            print("The size of each bicluster is {}".format(biclSizeList))
            print("The average value of the ASR Index for the set of biclusters is {}   -->   indicator of clustering accuracy".format(asrMean))
            print("The maximum overlap ratio of the biclusters is {}".format(maxRatio))
            print('Done \n------------------------------------------------------')

    #print(biclusters)

    #Compute time elapsed between start and end of execution
    print("---- %s seconds ----" % (time.time() - start_time))

    if config == "T":
        x = similarityRatio(biclusters)

    df.to_csv(txt + "RESULTS4.csv")

    #Move files to another repository
    for f in files:
        shutil.move(f, 'Outputs')

    print('All done!')