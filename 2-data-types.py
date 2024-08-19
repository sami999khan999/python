# string

# A string in Python is a sequence of characters enclosed in quotes. Strings can be created using single quotes ('), double quotes ("), or triple quotes (''' or """) for multi-line strings.

first_name = "Sami"
last_name = "Khan"

print(first_name)
print("Hello" + " " + first_name)

# The type function will pront the data type of a variable to the console window.
print(type(first_name))

# ===================================================================================================== #

# integer

# An integer is a whole number without a fractional part. In Python, integers can be positive, negative, or zero.
age = 20
age2 = 30

# This operation adds 1 to the current value of age and then assigns the result back to age. If age was initially 20, after this operation, age would be 21.
age += 1

print(age)
print(age + age2)
print(type(age))

# converts the integer age to a string and concatenates it with the message, then prints the complete sentence.
print("Your age is" + " " + str(age))

# ===================================================================================================== #

# float

# float is a numaric value that contains a decimal portion. An integer value can't sotre a decimal value.
pi = 3.14159

print(pi)
print(type(pi))

# ===================================================================================================== #

# boolean

# A Boolean in Python is a data type that can hold one of two values: True or False, representing truth values.
a = True
b = False

print(a)
print(type(b))
