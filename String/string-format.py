# string format

# The format() method in Python is used to format strings by inserting values into placeholders. It provides a flexible way to create well-structured and readable strings by embedding variables directly in the string.

name = "John"
age = 30

print("This is {}. He is {} years old".format(name, age))

# ===================================================================================================== #

# Positional Arguments

# You can specify the order of arguments using numbered placeholders.

print("The {1} jumped over the {0}.".format("moon", "cow"))
print("The {1} jumped over the {1}.".format("moon", "cow"))

# ===================================================================================================== #

# Named (Keyword) Arguments

# You can also use named arguments for more readable and flexible string formatting.

print("My name is {name} and I am {age} years old.".format(name="Sami", age=22))

# ===================================================================================================== #

# Alignment

# You can align text or numbers using format() with < for left alignment, > for right alignment, and ^ for center alignment.

print("My name is {:10}.".format("sami"))  # right alignment
print("My name is {:>10}.".format("sami"))  # left alignment
print("My name is {:^10}.".format("sami"))  # middle alignment

print("My name is {0:10}.".format("sami"))  # right alignment
print("My name is {name:>10}.".format(name="sami"))  # left alignment

# ===================================================================================================== #

# Formatting Numbers

# You can format numbers with precision or padding using the format() method.

pi = 3.14159

print("The number pi is {:.3f}".format(pi))
print("The number pi is {:.2f}".format(pi))
print("The number pi is {:.1f}".format(pi))

number = 1000

print("The number in {:,}".format(number))
print("The number in {:b}".format(number))  # binary format
print("The number in {:o}".format(number))  # octal format
print("The number in {:X}".format(number))  # hexadecimal format
print("The number in {:E}".format(number))  # sinetific format
