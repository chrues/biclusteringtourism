Biclustering for tourism

Necessary tools to run the programs:
- Java Virtual Machine
- Python (Version 3.7 or up)
- Source-code editor (Virtual Studio Code, Sublime Text, ...)
- Shell (Command Prompt, Git Bash, ...)
- Any version of Excel

Downloads:
- BicFinder.jar
- BiMine+.jar
- jarCall.py
- operationsMissingData.py
- removeCategories.py
- csvToText.py 

Important notes: Make sure they are all located in the same directory and inside of that directory create a folder called "Outputs". This is where all of your outputs will be stored.

How to run the executables directly (BicFinder, BiMine+, Bicat): 
  1) Open shell
  2.1) For BicFinder:
       BicFinder.jar InputFile.txt ACSI ASR OutputFile.txt
       where:
        - InputFile.txt is the microarray dataset. Each line must contain only gene name with their
          expression values. The condition names must be removed (see Input File Format). Missing
          values are replaced by random values.
        - ACSI is the threshold of the average correspondence similarity index (ACSI  [0..1]).
        - ASR is the threshold of the average spearman’s rho (ASR  [-1..1]).
        - OutputFile.txt is the result file. Each line contains one bicluster. One bicluster contains a
          subset of genes, a subset of conditions and ASR value.
          
  2.2) For BiMine+:
       BiMine+.jar InputFile.txt δ β OutputFile.txt
       where:
        - InputFile.txt is the microarray dataset. Each line must contain only gene name with their
          expression values. The condition names must be removed (see Input File Format). Missing
          values are replaced by random ones.
        - δ is the threshold of minimum number of conditions.
        - β is the threshold of the Average Spearman’s Rho (ASR  [-1..1]).
        - OutputFile.txt is the result file. Each line contains one bicluster. One bicluster contains a
          subset of genes, a subset of conditions and the ASR value. The conditions are considered as a
          number. In fact, the conditions numbering start from 0, e.g., the first condition in the InputFile
          is transformed in the OutputFile to 0, the second condition to 1, etc.
          
 The [Executable name].jar and the InputFile.txt must be in the same directory. The OutputFile will be created in the same directory.

How to call executables indirectly (from Python):
  1) Open source-code editor
  2) Open and execute the main module
  3) You will be ask to pre-process data files (which you can deny)
  4) You will be prompted to enter name of executable of your desire and the text file you would like to pass as an argument (omit .txt)
  5) Text file will be iterated for parameters A 2, 4 and 6, and parameters B between -0.6 and 0.6
  6) Shortly biclusters should be created and data statistics will be printed
  7) Output files will be moved to folder "Outputs"

Important note: Make sure the data files contain no missing values and no text
