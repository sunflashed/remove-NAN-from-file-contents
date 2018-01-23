import os

filelist = os.listdir() # creates list of all files in the current directory
for file in filelist: # loops through all files in the previously created list...
    if file.endswith(".txt"): # ...but only applies the following if they are a .txt
        f = open(file, "r") # opens the file in read mode
        lines = f.readlines() # stores each line of the file
        f.close() # closes the file
        f = open(file, "w") # opens the file in write mode
        for line in lines: # goes line-by-line
            if 'NAN' not in line: # if NAN is NOT in the line, it writes it - thus skipping the line with NAN
                f.write(line)
        f.close() # closes the file
