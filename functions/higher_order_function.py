# ---------------------------
# Functions as Arguments (Higher-Order Functions)
# ---------------------------
# Functions can accept other functions as arguments.
# This allows for dynamic behavior where the called function can vary based on the input function.


# Example: Function that accepts another function to modify text
def loud(text):
    """Returns the text in uppercase."""
    return text.upper()


def quiet(text):
    """Returns the text in lowercase."""
    return text.lower()


def hello(func, text):
    """Applies the given function (func) to the text and prints the result."""
    text = func(text)
    print(text)


# Calling the 'hello' function with different behavior
hello(quiet, "Hello")  # Output: hello
hello(loud, "Hello")  # Output: HELLO

# Explanation:
# The 'hello' function accepts another function (either 'loud' or 'quiet') and applies it to the given text.
# This showcases the flexibility of higher-order functions, which can receive functions as parameters.

# ---------------------------
# Returning Functions (Closures)
# ---------------------------
# Functions can return other functions.
# This is useful when you need to generate functions dynamically with specific behavior.


# Example: Function that returns a function (closure)
def devisor(x):
    """Returns a function that divides by x."""

    def dividend(y):
        return y / x

    return dividend


# Creating a function that divides by 5
divide = devisor(5)

# Using the returned function
print(divide(10))  # Output: 2.0

# Explanation:
# The 'devisor' function returns another function, 'dividend', which divides by the value of 'x'.
# This technique is known as a closure, where the returned function retains access to the variables of its parent function.
