import time

# for loop

# The for loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence. It is commonly used when you know in advance how many times you want to iterate.

# ===================================================================================================== #

# for i in range(10):
#   print(i)

# ===================================================================================================== #

# for i in range(1, 10+1):
#   print(i)

# ===================================================================================================== #

# name = "sami"

# for i in name:
#   print(i)

# ===================================================================================================== #

# for i in range(0, 100+5, 5):
#   print(i)

# ===================================================================================================== #

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)  # pause for 1 second before printing the next number

print("Happy new Year!")
