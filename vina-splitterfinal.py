#Title            :vina-splitter.py
#Description      :iterates over all files in a directory and separates poses from pdbqt output file
#Author           :Carter Gottschalk(https://github.com/cgott98)
#Date             :2019-02-20
#Version          :0.3
#Notes            :Special thank you to Matt Ritzinger(https://github.com/mritzing) for extensive help
#=====================================================================================================#

import os # Import necessary os module

cwd = os.getcwd() #retrieves current directory that the script is in
new_dir = "/home/yanbosmu/zinctest4"
os.mkdir(new_dir)
for file in os.listdir(cwd): #iterates through all files in current directory
    filename = os.fsdecode(file)
    if filename.endswith(".pdbqt"): #only opens pdbqt files
        
        with open(filename) as f:
            first_line = f.readline()
            if first_line[:5] == "MODEL": #checks to see if pdbqt is a vina output and not an autodock pdbqt file
                reading_file = open(filename, "r")
                baseFileName = os.path.splitext(filename)[0]; # = file name ending with pdbqt
                for line in reading_file:
                    if "ENDMDL" not in line: 
                        if line[:5] == "MODEL":
                            count = line[6:].rstrip()
                            fName = baseFileName+"_model_" + str(count) + ".pdb" #names file based on model number
                            new_file_path = os.path.join(new_dir, fName)
                            writing_file = open(new_file_path, "w")
                        elif "Si" in line:
                            line = line.replace('Si', 'C')
                            writing_file.write(line)
                        else:
                            writing_file.write(line)
                    else:
                        writing_file.close() # close current file open new one
            else:
                continue
    else:
        continue
