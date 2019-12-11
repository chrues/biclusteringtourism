import csv
import shutil
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir('Temp') if isfile(join('Temp', f))]

for f in onlyfiles:
    csv_file = f
    txt_file = f[0:len(f)-4] + '.txt'
    with open(txt_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
           [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
        my_output_file.close()
