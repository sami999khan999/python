# file detection

# File detection involves checking whether a file or directory exists, its type, and other attributes. Python provides several modules and functions to handle file detection, primarily using the os and pathlib modules.

import os

path = "C:\\Users\\sami9\\Downloads\\Documents"

if os.path.exists(path):
    print("This file location exists.")

    if os.path.isfile(path):
        print("This is a file.")
    elif os.path.isdir(path):
        print("This is a directory.")

else:
    print("This file location does not exist.")
