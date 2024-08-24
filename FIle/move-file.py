# moving a file

# To move a file from one directory to another using the os module, you essentially need to provide the new path (which includes the destination directory) and use os.rename() to perform the move operation.

import os

source_path = "text.txt"
destination_path = "D:\Code\Python\python-notes\\text.txt"

try:
    if os.path.exists(destination_path):
        print("This path already exists!")
    else:
        os.replace(source_path, destination_path)
        print(source_path + " was moved.")
except FileNotFoundError:
    print(source_path + " was not found.")
