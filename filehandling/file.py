# ---------------------------
# Creating a File
# ---------------------------
# You can create a new file in Python using the built-in 'open' function with the 'w' (write) or 'x' (exclusive creation) mode.

# Example: Creating a new file
file_name = "example.txt"

# Create a new file (will raise an error if the file already exists)
with open(file_name, "x") as file:
    file.write("This is a new file.")  # Write content to the file

# Explanation:
# The 'open' function with 'x' mode creates a new file and raises a FileExistsError if the file already exists.
# You can also use 'w' mode to create a new file or overwrite an existing one.

# Use Case:
# Creating a log file to store application events or errors. For instance, a web server might create a log file to keep track of requests.

# ---------------------------
# Reading from a File
# ---------------------------
# You can read the contents of a file using the 'open' function in 'r' (read) mode.

# Example: Reading the entire content of a file
with open(file_name, "r") as file:
    content = file.read()  # Read the entire content of the file
    print(content)  # Output: This is a new file.

# Example: Reading a single line from a file
with open(file_name, "r") as file:
    line = file.readline()  # Read the first line of the file
    print(line)  # Output: This is a new file.

# Explanation:
# The 'open' function with 'r' mode opens the file for reading.
# The 'read' method reads the entire content of the file as a string.
# The 'readline' method reads one line from the file.
# Always remember to close the file after completing the operations, though using 'with' handles that automatically.

# Use Case:
# Reading configuration settings from a file, such as database connection details, to initialize an application.

# ---------------------------
# Writing to a File
# ---------------------------
# You can write to a file using the 'open' function in 'w' (write) or 'a' (append) mode.

# Example: Writing to a file
with open(file_name, "a") as file:  # Open in append mode
    file.write("\nAppending this line.")  # Append content to the file

# Example: Writing a single line to a file
with open(file_name, "w") as file:  # Open in write mode (overwrites existing content)
    file.write("This is a new line written to the file.\n")  # Write a single line

# Reading updated file content
with open(file_name, "r") as file:
    content = file.read()
    print(content)  # Output: This is a new line written to the file.

# Explanation:
# The 'open' function in 'a' mode opens the file for appending, allowing you to add content without overwriting existing data.
# If you use 'w' mode instead, it will overwrite the existing content.
# The 'write' method writes a string to the file. You can use newline characters (`\n`) to separate lines.

# Use Case:
# Writing data to a CSV file for exporting user information from an application, enabling easy import into spreadsheets.

# ---------------------------
# Renaming a File
# ---------------------------
# You can rename a file using the 'os' module, specifically the 'rename' function.

import os

# Example: Renaming a file
new_file_name = "renamed_example.txt"
os.rename(file_name, new_file_name)  # Rename the file

# Explanation:
# The 'os.rename' function takes the current file name and the new file name as arguments.
# If the new file name already exists, it will raise a FileExistsError.

# Use Case:
# Renaming a temporary file after processing it to reflect its new status or content, such as changing "temp.txt" to "final_report.txt".

# ---------------------------
# Deleting a File
# ---------------------------
# You can delete a file using the 'os' module with the 'remove' function.

# Example: Deleting a file
os.remove(new_file_name)  # Delete the file

# Explanation:
# The 'os.remove' function deletes the specified file. If the file does not exist, it raises a FileNotFoundError.
# Always ensure that you want to delete a file, as this operation is irreversible.

# Use Case:
# Deleting temporary files generated during a data processing task to free up disk space and keep the directory organized.

# ---------------------------
# Copying a File
# ---------------------------
# You can copy a file using the 'shutil' module, specifically the 'copy' function.

import shutil

# Example: Copying a file
copy_file_name = "copy_of_example.txt"
shutil.copy(new_file_name, copy_file_name)  # Copy the renamed file to a new file

# Reading the copied file content
with open(copy_file_name, "r") as file:
    copied_content = file.read()
    print(copied_content)  # Output: This is a new line written to the file.

# Explanation:
# The 'shutil.copy' function copies the contents of the source file to the destination file.
# It creates a new file with the specified name, containing the same content as the source file.

# Use Case:
# Creating backups of important files regularly to prevent data loss in case of accidental deletion or corruption.
