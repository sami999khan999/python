# while loop

# The while loop in Python is used to repeatedly execute a block of code as long as a given condition is True. It is ideal for situations where you want to keep looping until a specific condition changes.

# ===================================================================================================== #

num = 1

while num <= 5:
    print("loop")
    num += 1

# ===================================================================================================== #

name = ""

while len(name) == 0:
    name = input("Please enter your name: ")

print("Hello," + name)

# ===================================================================================================== #

count = 0

while count <= 10:
    if count == 4:
        break
    print(count)
    count += 1
