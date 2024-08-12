# The math module in Python provides mathematical functions and constants. It is part of the standard library and offers a variety of operations for advanced mathematical computations.

import math

pi = 3.1416

# ===================================================================================================== #

# The round() function in Python is used to round a floating-point number to a specified number of decimal places. If no number of decimal places is specified, it rounds to the nearest integer.

print(round(pi))
print(round(pi, 2))

# ===================================================================================================== #

# The math.ceil() function returns the smallest integer greater than or equal to a given number. It is useful for rounding up numbers to the nearest whole number.

print(math.ceil(pi))

# ===================================================================================================== #

# The math.floor() function returns the largest integer less than or equal to a given number. It is useful for rounding down numbers to the nearest whole number.

print(math.floor(pi))

# ===================================================================================================== #

# The abs() function in Python returns the absolute value of a number. The absolute value is the non-negative value of the number, which means it strips away any negative sign.

print(abs(pi))

# ===================================================================================================== #

# The pow() function in Python is used to raise a number to a specified power or to calculate the result of a number raised to a power with an optional modulus.

print(pow(pi,2))

# ===================================================================================================== #

# The sqrt() function in Python computes the square root of a number. It is part of the math module.

print(math.sqrt(pi))

# ===================================================================================================== #

# The max() and min() functions in Python are used to find the largest and smallest values, respectively, from a set of values or within a sequence like a list or tuple.

x = 1
y = 2
z = 3

print(max(x,y,z))
print(min(x,y,z))