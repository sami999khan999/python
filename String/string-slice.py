# slicing

# String slicing allows you to create a substring by extracting a portion of a string using a specific range of indices. Slicing can be done using the syntax string[start:stop:step]

# start: The starting index (inclusive). Defaults to 0 if not provided.
# stop: The ending index (exclusive). Required.
# step: The step between each index. Defaults to 1 if not provided.

name = "samikhan"

first_name = name[0:4]
last_name = name[4:8]
another_name = name[0:8:2]

print(first_name)
print(last_name)
print(another_name)

# ===================================================================================================== #

# reverse

# Reversing a string in Python can be done easily using string slicing, which allows you to create a new string by specifying the slice's start, stop, and step values. You can reverse a string by slicing it with a step of -1, which starts from the end of the string and moves backward.

reversed_name = name[::-1]

print(reversed_name)
