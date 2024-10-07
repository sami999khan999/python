# ---------------------------
# Creating a Directory
# ---------------------------
# You can create a new directory in Python using the 'os' module with the 'mkdir' or 'makedirs' function.

import os

# Example: Creating a new directory
directory_name = "example_directory"

# Create a new directory
os.mkdir(directory_name)  # Will raise an error if the directory already exists

# Explanation:
# The 'os.mkdir' function creates a new directory with the specified name.
# If you want to create nested directories, you can use 'os.makedirs'.

# Use Case:
# Creating a directory to organize project files, such as separating images, scripts, and documentation.

# ---------------------------
# Reading a Directory
# ---------------------------
# You can read the contents of a directory using the 'os' module with the 'listdir' function.

# Example: Reading a directory
contents = os.listdir(directory_name)  # List the contents of the directory
print(contents)  # Output: []

# Explanation:
# The 'os.listdir' function returns a list of the names of the entries in the specified directory.
# This includes files and subdirectories.

# Use Case:
# Reading a directory to display available files for user selection in a file management application.

# ---------------------------
# Writing to a File in a Directory
# ---------------------------
# You can write a file to a specific directory using the 'open' function with the full file path.

# Example: Writing to a file in a directory
file_path = os.path.join(directory_name, "file_in_directory.txt")  # Create a file path

with open(file_path, "w") as file:  # Open in write mode
    file.write("This file is inside the directory.")  # Write content to the file

# Explanation:
# The 'os.path.join' function creates a full file path by joining the directory name and the file name.
# This ensures the correct file path regardless of the operating system.

# Use Case:
# Saving configuration or data files in a specific directory to keep the project organized.

# ---------------------------
# Renaming a Directory
# ---------------------------
# You can rename a directory using the 'os' module with the 'rename' function.

# Example: Renaming a directory
new_directory_name = "renamed_directory"
os.rename(directory_name, new_directory_name)  # Rename the directory

# Explanation:
# The 'os.rename' function takes the current directory name and the new directory name as arguments.
# If the new directory name already exists, it will raise a FileExistsError.

# Use Case:
# Renaming a directory to reflect its updated purpose, such as changing "old_files" to "archived_files".

# ---------------------------
# Deleting a Directory
# ---------------------------
# You can delete a directory using the 'os' module with the 'rmdir' function.

# Example: Deleting a directory
os.rmdir(new_directory_name)  # Delete the directory (must be empty)

# Explanation:
# The 'os.rmdir' function removes the specified directory. The directory must be empty, or it will raise an OSError.
# If you need to delete a directory with contents, use 'shutil.rmtree'.

# Use Case:
# Deleting temporary directories created during a process to keep the workspace clean.

# ---------------------------
# Read Files Name From Directory and Print List
# ---------------------------
# You can read file names from a directory and print them using the 'os' module.

# Example: Reading and printing file names from a directory
# Assuming there are files in the directory for demonstration purposes
file_names = os.listdir(new_directory_name)  # List the files in the directory
print("Files in directory:", file_names)

# Explanation:
# The 'os.listdir' function retrieves the list of files and subdirectories in the specified directory.
# You can loop through this list to process or print the names of the files.

# Use Case:
# Displaying a list of available files to users for selection or further processing in an application.
