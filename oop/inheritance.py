# Inheritance:
# Inheritance is a feature of object-oriented programming that allows one class (subclass/child class)
# to inherit the properties and methods from another class (parent class).
# This promotes code reusability, as child classes can use or modify the methods and attributes of the parent class.


# Define a base class 'Animal'
# This class serves as the "parent" class for all other animal types.
class Animal:
    # Constructor method (__init__) initializes the object with 'name' and 'age'.
    # These attributes are unique to each instance of the class.
    def __init__(self, name, age):
        self.name = name  # Assign 'name' to the instance
        self.age = age  # Assign 'age' to the instance

    # Define a method 'eat' to describe the action of eating
    def eat(self):
        print(
            f"This {self.name} is {self.age} years old, and he is eating"
        )  # Print the animal's name and age when eating

    # Define another method 'sleep' to describe the action of sleeping
    def sleep(self):
        print(
            f"This {self.name} is {self.age} years old, and he is sleeping"
        )  # Print the animal's name and age when sleeping


# Define a 'Dog' class that inherits from 'Animal'
# This means 'Dog' has all the methods and attributes of 'Animal'
class Dog(Animal):
    # No additional methods or attributes are defined, so it uses everything from 'Animal'
    pass  # 'pass' means no additional functionality is added


# Define a 'Cat' class that also inherits from 'Animal'
# Like 'Dog', 'Cat' will inherit the properties and methods from the 'Animal' class
class Cat(Animal):
    pass  # 'pass' means no additional functionality is added


# Creating instances (objects) of the 'Dog' and 'Cat' classes

# Create a 'Dog' object with a name "Dog" and age 9
dog = Dog("Dog", 9)

# Call the 'sleep' method inherited from the 'Animal' class
# Output: "This Dog is 9 years old, and he is sleeping"
dog.sleep()

# Create a 'Cat' object with a name "Cat" and age 4
cat = Cat("Cat", 4)

# Call the 'eat' method inherited from the 'Animal' class
# Output: "This Cat is 4 years old, and he is eating"
cat.eat()


# Key Points:
# 1. Inheritance allows a child class to acquire methods and attributes from a parent class.
# 2. The 'Dog' and 'Cat' classes inherit from 'Animal' without redefining its methods.
# 3. The 'pass' statement indicates that no additional functionality is needed in the child classes.
# 4. The 'Animal' class defines general methods (e.g., 'eat' and 'sleep') that can be shared among subclasses.
# 5. Inheritance promotes code reusability and allows for hierarchical relationships between classes.
