import csv
import shutil

def conversion():
    """Ports comma-separated value file to text file using the module "shutil" 
       And removes header row so file can be processed"""
    
    csv_file = input('Enter the name of your input file: ')
    txt_file = input('Enter the name of your output file: ')
    with open(txt_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
        my_output_file.close()
    
    f1 = open(txt_file, "r")
    lines = f1.readlines()
    entries = ""
    f1.close()

    for i in range(1, len(lines)):
        entries += lines[i]
    f2 = open(txt_file, "w")
    f2.write(entries)
    f2.close()