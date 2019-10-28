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
  2) Enter following line: java -jar [Name of executable].jar [Input file] [The minimum amount of columns to be evaluated inside a dataset] [Average Spearman Index ranging between -1 and 1] [Output file].
Upon execution the results will be written to your output file.

How to call executables indirectly (from Python) using jarCall.py:
  1) Open source-code editor
  2) Open and execute jarCall.py
  3) You will be prompted to enter name of executable of your desire and the text file you would like to pass as an argument (omit .txt)
  4) Text file will be iterated for parameters A 2, 4 and 6, and parameters B between -0.6 and 0.6
  5) Output files will be moved to folder "Outputs"

Important note: If your data presents anomalies such as missing data and non-numerical values, you must run programs operationsMissingData.py and/or removeCategories.py


