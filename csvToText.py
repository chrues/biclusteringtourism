import csv
import shutil

csv_file = input('Enter the name of your input file: ')
txt_file = input('Enter the name of your output file: ')
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()