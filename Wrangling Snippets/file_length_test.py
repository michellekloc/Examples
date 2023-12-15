#The technician manually cutting files made some mistakes, missing filenames in some folders, so there were files of different lengths. For this analysis, this is a problem.

import os

folders = ["Path1", "Path2"]
for i in folders:
    def get_files_with_extension(directory, extension):
        files = []
        for root, dirs, filenames in os.walk(directory):
            for filename in filenames:
                if filename.endswith(extension):
                    files.append(os.path.join(root, filename))
        return files
    
    def are_files_same_size(files):
        sizes = []
        for file in files:
            size_kb = os.path.getsize(file) / 1024
            sizes.append(size_kb)
        return len(set(sizes)) == 1
    
    # Directory where the files are located
    directory = i
    
    # File extension to compare sizes
    extension = ".ncs"
    
    # Get all files with the specified extension in the directory
    files = get_files_with_extension(directory, extension)
    
    # Check if files have the same size
    if are_files_same_size(files):
        #print(f"All {extension} files have the same size.")
        pass
    else:
        print(f"{extension} files have different sizes." + i)
