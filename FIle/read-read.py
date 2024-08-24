# read file

# Reading a file in Python is simple using the open() function or the with statement. There are several ways to read the content of a file depending on the requirement: reading the entire file at once, reading line by line, or reading a specific number of characters.

with open("text.txt") as file:
    content = file.read()
    print(content)

# ===================================================================================================== #

# readline

# read the file line by line, you can use the readline() method.

with open("text.txt") as file:
    content = file.readline()
    while content:
        print(content)
        content = file.readline()

# ===================================================================================================== #

# readlines

# You can also read all lines at once into a list using the readlines() method. Each element in the list corresponds to one line of the file.

with open("text.txt", "r") as file:
    content = file.readlines()
    for line in content:
        print(line)
