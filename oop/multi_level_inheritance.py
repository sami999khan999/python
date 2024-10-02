# Multi-level Inheritance:
# Multi-level inheritance is a type of inheritance where a class inherits from another derived class,
# forming a chain of inheritance. In this example:
# - The 'Organisom' class is the base class (top of the hierarchy).
# - The 'Animal' class inherits from 'Organisom' (intermediate class).
# - The 'Dog' class inherits from 'Animal' (derived class).


# Base Class: Organism
class Organisom:
    alive = True  # Class attribute, all organisms are considered alive


# Intermediate Class: Animal
# The 'Animal' class inherits from 'Organisom', so it also gets the 'alive' attribute.
class Animal(Organisom):
    def walk(self):
        print("This animal is walking.")


# Derived Class: Dog
# The 'Dog' class inherits from 'Animal', so it gets both the 'alive' attribute and the 'walk' method.
class Dog(Animal):
    def bark(self):
        print("This dog is barking.")


# In multi-level inheritance, the 'Dog' class indirectly inherits from 'Organisom' through 'Animal'.
# This means 'Dog' has access to both the 'alive' attribute from 'Organisom' and the 'walk' method from 'Animal'.

# Creating an instance of the Dog class
dog = Dog()

# Accessing attributes and methods from the entire inheritance chain:
print(dog.alive)  # Output: True (inherited from the 'Organisom' class)
dog.walk()  # Output: This animal is walking. (inherited from the 'Animal' class)
dog.bark()  # Output: This dog is barking. (defined in the 'Dog' class)

# Explanation of Multi-level Inheritance:
# 1. The 'Dog' class inherits from 'Animal', which in turn inherits from 'Organisom'.
# 2. The 'Dog' class can access attributes and methods from both its parent ('Animal') and grandparent ('Organisom').
# 3. This forms a chain of inheritance: Organisom -> Animal -> Dog.
# 4. Multi-level inheritance helps to model relationships where a class depends on several layers of functionality.
