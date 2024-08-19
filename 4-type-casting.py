# Typecasting (or type conversion) in Python refers to converting one data type into another. This can be done using built-in functions to ensure that variables are of the expected type, especially when performing operations that require specific types.

x = 1  # integer
y = 2.1  # float
z = "3"  # string

# ===================================================================================================== #

y = int(y)  # float to integer
z = int(z)  # string to integer

print(y, z)

# ===================================================================================================== #

x = float(x)  # integer to float
z = float(z)  # string to float

print(x, z)

# ===================================================================================================== #

x = str(x)  # integer to string
y = str(y)  # float to string

print(x, y)
