import pandas as pd
import csvToText
from operations_missingData import averageValue, assignMin_Max, assignNeutralValue, labelEncoding

def preprocessing():
   converting = True
   while True:  
      filename = input("Enter the name of the file: ")
      df = pd.read_csv(filename, engine = 'python')
      method = input('Choose the method with which you would like to replace the non values (A, B, C, D): ')

      if method == 'A':
         averageValue(df)
      elif method == 'B':
         assignMin_Max(df)
      elif method == 'C':
         assignNeutralValue(df)
      elif method == 'D':
         labelEncoding(df)

      running = input("Continue pre-processing data? (True/False)")
      if running == "False":
         break

      print("----------------------------------------------------------------------------------------------------------")

   print("Proceeding to convert .csv file(s) to text file(s)...")
   while converting:
      csvToText.conversion()
      converting = input("Continue converting? (True/False)")