# ---------------------------
# Basic Lambda Function
# ---------------------------
# A lambda function is a small anonymous function defined using the 'lambda' keyword.
# Lambda functions can take any number of arguments but can only have one expression.

# Example: Basic lambda function to double a number
double = lambda x: x * 2

# Calling the lambda function
print(double(5))  # Output: 10

# Explanation:
# The 'double' lambda function takes one argument 'x' and returns its double.
# Lambda functions are often used for short, simple operations without the need to define a full function.

# ---------------------------
# Lambda for Simple Calculations
# ---------------------------
# Lambda functions are particularly useful for simple calculations or transformations.

# Example: Using lambda to create a function for squaring a number
square = lambda x: x**2

# Example: Using lambda with the 'map' function
numbers = [1, 2, 3, 4]
squared_numbers = list(map(square, numbers))  # Squaring each number in the list
print(squared_numbers)  # Output: [1, 4, 9, 16]

# Explanation:
# The 'square' lambda function squares a number. The 'map' function applies this lambda to each element in the 'numbers' list.
# This showcases how lambda functions can be used in functional programming styles for concise transformations.

# ---------------------------
# When to Use Lambda Functions
# ---------------------------
# Lambda functions are useful in situations where you need a simple function for a short duration,
# especially as arguments to higher-order functions like 'map', 'filter', and 'sorted'.

# Example: Using lambda with 'sorted' to sort by the second element in tuples
data = [(1, 2), (3, 1), (5, 0)]
sorted_data = sorted(data, key=lambda x: x[1])  # Sorts based on the second element
print(sorted_data)  # Output: [(5, 0), (3, 1), (1, 2)]

# Explanation:
# In this example, the lambda function is used as a key function for sorting.
# It is concise and keeps the code readable without needing a separate function definition.

# ---------------------------
# When Not to Use Lambda Functions
# ---------------------------
# Lambda functions should not be used for complex operations that require multiple expressions or statements,
# as they can reduce code readability and maintainability.


# Example: A complex function that is better defined as a standard function
def complex_operation(x, y):
    """Returns the result of a complex operation."""
    if x > y:
        return x + y
    else:
        return x * y


# Trying to use a lambda for the same operation would be convoluted and less clear
# complex_lambda = lambda x, y: (x + y if x > y else x * y)  # Less readable

# Explanation:
# While you could technically write a complex operation as a lambda, it's usually better to use a standard function
# for clarity and to accommodate multiple statements, which lambda cannot handle.
