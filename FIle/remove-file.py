# remove file

# To delete files and folders in Python, you can use functions from the os and shutil modules.

import os

# ===================================================================================================== #

# remove file

# You can use the os.remove() function to delete a file.

path = "text.txt"

try:
    os.remove(path)
    print("File deleted successfully.")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")

# ===================================================================================================== #

# remove folder

# You can use the os.rmdir() function to delete a file. This only deletes empty folders.

path = "f"

try:
    os.rmdir(path)
    print("Folder deleted successfully.")
except FileNotFoundError:
    print("Folder not found.")
except OSError:
    print("Couldn't delete this floder.")
except PermissionError:
    print("Permission denied.")
