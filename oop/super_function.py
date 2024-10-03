# super() Function:
# The super() function in Python allows access to methods of the parent class.
# It is used primarily in inheritance to refer to the parent class without needing to explicitly name it.
# In the context of class inheritance, super() helps in calling the parent class's methods and constructors.
# This is useful when you want the child class to extend or modify the functionality of the parent class but still retain
# some of its original behaviors. It promotes code reusability and avoids repeating the parent class's logic in the child class.


# Class: Shape
# The Shape class is the base (or parent) class that defines general properties of a shape, such as 'color' and 'filled' status.
class Shape:
    def __init__(self, color, filled):
        self.color = color  # Every shape has a color (e.g., red, blue)
        self.filled = filled  # Every shape can be filled (True) or not filled (False)


# Class: Circle (inherits from Shape)
# The Circle class is a subclass (child class) that inherits the properties and methods from the Shape class.
class Circle(Shape):
    # Constructor (__init__) for Circle, which also initializes 'color' and 'filled' from the parent class Shape.
    def __init__(self, color, filled, radius):
        # The super() function calls the __init__ method of the parent class (Shape).
        # This initializes the 'color' and 'filled' attributes in the Circle class.
        super().__init__(
            color, filled
        )  # super() ensures that the constructor of the parent class is called
        self.radius = radius  # Circle-specific attribute: radius

    # Method to calculate the area of the circle (πr^2).
    def area(self):
        print(f"The area of the circle is {3.1415 * self.radius * self.radius}")


# Class: Square (inherits from Shape)
# The Square class also inherits from the Shape class, just like the Circle class.
class Square(Shape):
    # Constructor (__init__) for Square, which also initializes 'color' and 'filled' from the parent class Shape.
    def __init__(self, color, filled, width):
        # The super() function is used to call the parent class's __init__ method to initialize 'color' and 'filled'.
        super().__init__(color, filled)  # Calls the Shape class constructor
        self.width = width  # Square-specific attribute: width

    # Method to calculate the area of the square (width * width).
    def area(self):
        print(f"The area of the square is {self.width * self.width}")


# Creating an instance of Circle and calculating its area
circle = Circle("Red", True, 4)
circle.area()  # Output: The area of the circle is 50.264
print(circle.color)  # Output: Red (inherited from Shape class)
print(circle.filled)  # Output: True (inherited from Shape class)

# Creating an instance of Square and calculating its area
square = Square("Blue", False, 5)
square.area()  # Output: The area of the square is 25
print(square.color)  # Output: Blue (inherited from Shape class)
print(square.filled)  # Output: False (inherited from Shape class)


# Explanation of the super() function:
# 1. The super() function is used in the child class (Circle and Square) to call the parent class (Shape)'s __init__ method. This ensures that the attributes 'color' and 'filled', which are defined in the Shape class, are properly initialized when creating an instance of the Circle or Square class.

# 2. Without super(), the child class would not automatically inherit and initialize these attributes, and we would have to manually set them for every child class. super() allows us to reuse the parent class's constructor, making our code more efficient and cleaner.

# 3. super() can also be used to call methods from the parent class that are overridden in the child class, but in this case, we only use it to call the parent class's constructor (__init__).
