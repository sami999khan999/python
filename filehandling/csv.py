# ---------------------------
# Make CSV File From List
# ---------------------------
# You can create a CSV file from a list using the 'csv' module.

import csv

# Example: Creating a CSV file from a list
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"],
]

csv_file_name = "example.csv"

# Write the list to a CSV file
with open(csv_file_name, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)  # Create a CSV writer object
    writer.writerows(data)  # Write all rows to the CSV file

# Explanation:
# The 'csv.writer' function creates a writer object, which is used to write data to a CSV file.
# The 'writerows' method writes multiple rows at once. Each sub-list in 'data' corresponds to a row in the CSV.

# Use Case:
# Creating a CSV file from structured data, such as user information or records, for easy import into spreadsheets.

# ---------------------------
# Make List From CSV File
# ---------------------------
# You can read a CSV file and convert its content into a list using the 'csv' module.

# Example: Reading a CSV file into a list
csv_file_name = "example.csv"

# Read the CSV file and convert it to a list
with open(csv_file_name, "r") as csv_file:
    reader = csv.reader(csv_file)  # Create a CSV reader object
    data_from_csv = list(reader)  # Convert the reader object to a list

# Display the contents of the list
print(data_from_csv)

# Explanation:
# The 'csv.reader' function creates a reader object that iterates over lines in the specified CSV file.
# Converting the reader object to a list collects all rows into a list of lists.

# Use Case:
# Importing data from a CSV file into a Python application for processing, analysis, or manipulation.
