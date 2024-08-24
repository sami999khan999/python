# exception handling

# Exception handling in Python allows you to gracefully handle errors that occur during the execution of your program. Instead of the program crashing when an error occurs, you can "catch" and manage the error using exception handling constructs.

try:
    x = 5
    y = 0
    print(x / 0)
except Exception:
    print("Something went wrong!")

# ===================================================================================================== #

# ZeroDivisionError

# ZeroDivisionError occurs when you try to divide a number by zero. In the example above, the code attempts to divide x by 0, resulting in a ZeroDivisionError.

try:
    x = 5
    y = 0
    print(x / y)
except ZeroDivisionError:
    print("Cannot divide by zero!")

# ===================================================================================================== #

# ValueError

# ValueError occurs when a built-in function or method receives an argument that has the correct type but inappropriate value.

try:
    value = int(input("Enter a number:"))
    print(value)
except ValueError:
    print("Invalid input!")

# ===================================================================================================== #

# Catching Multiple Exceptions

#  You can catch multiple exception types using a tuple or multiple except blocks.

try:
    result = 10 / int(input("Enter a number: "))
except (ValueError, ZeroDivisionError) as e:
    print(f"Error occurred: {e}")

# ===================================================================================================== #

# finally Block

#  Runs regardless of whether an exception occurred or not. It’s useful for cleanup actions like closing files or releasing resources.

try:
    x = 5
    y = 0
    print(x / y)
except ZeroDivisionError:
    print("Can't divide by zero!")
finally:
    print("This will always print.")
