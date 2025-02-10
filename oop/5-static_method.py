class MathOperations:
    # Static methods are functions inside a class that don't require access to instance (self)
    # or class (cls) data. They are defined using the @staticmethod decorator.

    @staticmethod
    def add(x, y):
        # Returns the sum of x and y.
        return x + y

    @staticmethod
    def multiply(x, y):
        # Returns the product of x and y.
        return x * y


# Calling static methods directly from the class without creating an instance.
result_add = MathOperations.add(5, 3)
result_multiply = MathOperations.multiply(5, 3)

print(f"Addition result: {result_add}")
print(f"Multiplication result: {result_multiply}")

# Summary:
# - Static methods are defined with @staticmethod and do not take a 'self' or 'cls' parameter.
# - They function like regular functions but are grouped within a class for logical organization.
# - Static methods are useful when the method's functionality is related to the class but doesn't require
#   access to its attributes or other methods.
