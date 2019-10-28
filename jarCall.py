import subprocess
import shutil
import os.path

exec = ''
parametersA = [2, 4, 6]
files = []
validFile = False

def jarWrapper(exec, txt):
    inputFile = txt + '.txt'
    for i in range(0,len(parametersA)):
        for j in range(1, 7):
            paramA = parametersA[i]
            avgSprmnIndex = -0.6 + 0.2 * j
            outputFile = txt + '_results-' + str(exec) + '-' + str(paramA) + '_' + str(avgSprmnIndex) + '.txt'
            file = open(outputFile, 'w')
            print('Writing to',outputFile+'...')
            subprocess.call([exec, inputFile, str(paramA), str(avgSprmnIndex), outputFile], shell=True)
            file.close()
            files.append(outputFile)
            print('Done \n------------------------------------------------------')
    for f in files:
        shutil.move(f, 'Outputs')
    print('All done!')
        
while (not exec.lower() == 'bicfinder.jar' and not exec.lower() == 'bimine+.jar'):
    exec = input('Choose which java executable to run (BicFinder.jar, BiMine+.jar): ')
while (not validFile):
    txt = input('Choose text file to pass as argument (omit .txt): ')
    validFile = os.path.isfile(txt + '.txt')
    if (not validFile):
        print('File not found in current directory')

jarWrapper(exec, txt)


