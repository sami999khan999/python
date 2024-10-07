# ---------------------------
# Creating a Zip File
# ---------------------------
# You can create a ZIP file in Python using the 'zipfile' module.

import zipfile

# Example: Creating a ZIP file
zip_file_name = "example.zip"

# Create a new ZIP file and add files to it
with zipfile.ZipFile(zip_file_name, "w") as zip_file:
    zip_file.write("file_in_directory.txt")  # Add a file to the ZIP

# Explanation:
# The 'zipfile.ZipFile' function is used to create a new ZIP file. The "w" mode indicates that we want to write to the file.
# You can add files using the 'write' method, which adds the specified file to the ZIP.

# Use Case:
# Creating a ZIP file to compress multiple files for easier storage or sharing.

# ---------------------------
# Extract from Zip File
# ---------------------------
# You can extract files from a ZIP file using the 'zipfile' module.

# Example: Extracting from a ZIP file
with zipfile.ZipFile(zip_file_name, "r") as zip_file:
    zip_file.extractall("extracted_files")  # Extract all files to a directory

# Explanation:
# The 'zipfile.ZipFile' function in "r" mode opens the ZIP file for reading.
# The 'extractall' method extracts all files in the ZIP to the specified directory.

# Use Case:
# Extracting files from a ZIP archive for use in a project or application.

# ---------------------------
# Make Zip From Directory
# ---------------------------
# You can create a ZIP file from all files in a directory.

import os

# Example: Creating a ZIP file from a directory
directory_to_zip = "example_directory"

# Create a ZIP file from the contents of a directory
with zipfile.ZipFile("directory_zip.zip", "w") as zip_file:
    for foldername, subfolders, filenames in os.walk(
        directory_to_zip
    ):  # Walk through the directory
        for filename in filenames:
            file_path = os.path.join(foldername, filename)  # Get the full file path
            zip_file.write(
                file_path, arcname=os.path.relpath(file_path, directory_to_zip)
            )  # Add to ZIP

# Explanation:
# The 'os.walk' function allows you to traverse a directory tree.
# For each file found, 'zip_file.write' adds it to the ZIP, with 'arcname' preserving the relative path.

# Use Case:
# Creating a ZIP file of a project directory for distribution, ensuring all files are included.
