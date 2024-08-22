# return statement

# The return statement is used in a function to send a result (or multiple results) back to the caller. It also immediately terminates the function's execution. If no return statement is used, or if the return is empty, the function will return None by default.


def sum(num1, num2):
    return num1 + num2


print(sum(4, 8))
