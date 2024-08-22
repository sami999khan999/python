# *args

# *args is used in function definitions to allow the function to accept a variable number of positional arguments. The term "args" is just a name convention; you can use any name, but the * is required. When using *args, Python collects all the additional positional arguments into a tuple.


def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(
    add(
        2,
        5,
        4,
        78,
        2,
    )
)
