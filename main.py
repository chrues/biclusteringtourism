import time
import os.path
import csvToText
import jarCall
from preprocessing import preprocessing
from similarityRatio import similarityRatio

def run():
    """Main method"""

    exec = ""
    validFile = False

    #Choose bi-clustering algorithm of preference
    while (not exec.lower() == 'bicfinder.jar' and not exec.lower() == 'bimine+.jar'):
        exec = input('Choose which java executable to run (BicFinder.jar, BiMine+.jar): ')

    #Choose file to be read and executed on by chosen algorithm
    while (not validFile):
        txt = input('Choose text file to pass as argument (omit .txt): ')
        validFile = os.path.isfile(txt + '.txt')
        if (not validFile):
            print('File not found in current directory or file possibly a comma-separated values file')
            csvToText.conversion()

    #
    config = input("Enable comparison between bi-clusters (Y/N)? ")
    print("--------------------------------------------")

    #Start clocking the time by fixing starting point
    start_time = time.time()

    #Calls method of module jarCall
    jarCall.jarWrapper(exec, txt, config, start_time)

userInput = input("Pre-process data (Y/N)? ")
if userInput == "Y":
    preprocessing()

run()