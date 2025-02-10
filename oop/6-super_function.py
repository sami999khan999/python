# Parent class: Shape
# Defines common attributes (color and filled) for all shapes.
class Shape:
    def __init__(self, color, filled):
        self.color = color  # Every shape has a color (e.g., "red", "blue")
        self.filled = filled  # Every shape has a filled status (True/False)


# Child class: Circle (inherits from Shape)
class Circle(Shape):
    def __init__(self, color, filled, radius):
        # Call the parent class (Shape) __init__ to initialize 'color' and 'filled'
        super().__init__(color, filled)
        self.radius = radius  # Circle-specific attribute: radius

    # Calculate and display the area of the circle (π * r^2)
    def area(self):
        print(f"The area of the circle is {3.1415 * self.radius * self.radius}")


# Child class: Square (inherits from Shape)
class Square(Shape):
    def __init__(self, color, filled, width):
        # Call the parent class (Shape) __init__ to initialize 'color' and 'filled'
        super().__init__(color, filled)
        self.width = width  # Square-specific attribute: width

    # Calculate and display the area of the square (width * width)
    def area(self):
        print(f"The area of the square is {self.width * self.width}")


# Create an instance of Circle and display its area and inherited attributes.
circle = Circle("Red", True, 4)
circle.area()  # Output: The area of the circle is 50.264 (approximately)
print(circle.color)  # Output: Red (inherited from Shape)
print(circle.filled)  # Output: True (inherited from Shape)

# Create an instance of Square and display its area and inherited attributes.
square = Square("Blue", False, 5)
square.area()  # Output: The area of the square is 25
print(square.color)  # Output: Blue (inherited from Shape)
print(square.filled)  # Output: False (inherited from Shape)

# Explanation of the super() function:
# 1. super().__init__(color, filled) calls the constructor of the parent class (Shape)
#    from within the child classes (Circle and Square). This ensures that the common
#    attributes 'color' and 'filled' are properly initialized.
#
# 2. Without using super(), you would have to manually set 'color' and 'filled' in each child class,
#    leading to redundant code.
#
# 3. The super() function promotes code reusability and cleaner code by leveraging the parent's logic,
#    while still allowing the child class to add its own specific attributes (like radius or width).

# Summary:
# - The Shape class serves as the base class with common attributes.
# - Circle and Square inherit from Shape and use super() to initialize shared attributes.
# - Each child class adds its own unique properties and methods (e.g., area calculations).
# - The super() function simplifies calling parent methods and constructors, making inheritance more efficient.
