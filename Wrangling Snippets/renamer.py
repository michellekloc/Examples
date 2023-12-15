# This script goes into every subolder of the provided directory,
# copies the files into an "output" subdirectory and renames CSCX files into CSC_X files,
# and copies the CSC1.params file placed next to this Python file into each output directory.

import sys
import os
import shutil
import re

fileSeparator = "\\"

inputPath = sys.argv[1]
#inputPath = path to files
# Reminder to hard-code a windows path you'll need to escape the \ backslashes with \\
subfoldersToRename = [f.path for f in os.scandir(inputPath) if f.is_dir() ]  # https://stackoverflow.com/a/40347279, Python 3.5+ only!

paramsFileName = 'CSC_0.params'
paramsFile = sys.path[0] + fileSeparator + paramsFileName

if not os.path.isfile(paramsFile):
    print ("Params file to copy is not in same directory as this Python file, quitting....")
    quit()

if os.path.isdir(inputPath) is True:
	pass
else:
	print("ERROR: Given path is not a directory...")
	quit()

# Delete any MacOS preview files that exist:
def delete_DS_Store_files(path):
    if os.path.exists(path + fileSeparator + ".DS_Store"):
        os.remove(path + fileSeparator +".DS_Store")

delete_DS_Store_files(inputPath)


for subfolder in subfoldersToRename:
    delete_DS_Store_files(subfolder)
    subfolder = subfolder + fileSeparator  #doesn't have trailing slash in it, so add separator
    delete_DS_Store_files(subfolder)
    
    for root, dirs, files in os.walk(subfolder):  
        if len(files) < 64 or len(files) > 65:  
            print ("\n\n" + root + "\nFile count not equal to 64 + params (65), check the folder!   # files: " + str(len(files)) + "\n\n")
        else:
            try:
                outputDir = subfolder + "_renamed_copy" + fileSeparator

                os.mkdir(outputDir)
                shutil.copy(paramsFile, outputDir + paramsFileName)
                for filename in files:
                    try:
                        fileAbsPath = root + filename
                        print(fileAbsPath)
    
                        filepath, file_extension = os.path.splitext(fileAbsPath)
                        if file_extension != ".params":  # CHANGE THIS to the exact file extension of the params files
                            newCSCnumber = int(re.split("_", re.split("CSC", filename)[1])[0]) - 1
                            newFilePath = outputDir + "CSC_" + str(newCSCnumber) + file_extension
                            shutil.copy2(fileAbsPath, newFilePath)
                        else:  # Copy the Params file over
                            #newFilePath = root + "output" + fileSeparator + filename
                            #shutil.copy2(fileAbsPath, newFilePath)
                            pass
                    except:
                        "Couldn't process " + root + filename
            except FileExistsError:
                print ("\n\nOUTPUT folder exists for:" + root + "\nskipping...\n\n")
        