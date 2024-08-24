# write file

# You can also read all lines at once into a list using the readlines() method. Each element in the list corresponds to one line of the file.

# ===================================================================================================== #

# appent file

# If you want to add new content to the end of an existing file without overwriting it, use "a" (append mode).

with open("text.txt", "a") as file:
    file.write("\nNew line added\n")
    file.write("Another line added\n")

# ===================================================================================================== #

# overwrite file

# Using "w" (write mode) will overwrite the file if it exists, or create a new file if it doesn't.

with open("text.txt", "w") as file:
    file.write("This is the new content\n")
    file.write("This is another new line\n")

# ===================================================================================================== #

# writelines

# You can also write multiple lines using a list and the writelines() method. Note that writelines() does not add newline characters automatically, so you need to include them in each string.

lines = ["First line\n", "Second line\n", "Third line\n"]

with open("text.txt", "a") as file:
    file.writelines(lines)
