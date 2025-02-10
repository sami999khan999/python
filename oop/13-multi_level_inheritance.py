# Multi-level Inheritance Example:
# Multi-level inheritance occurs when a class is derived from another derived class,
# forming a chain of inheritance. In this example:
# - The base class 'Organisom' (intended as 'Organism') defines general properties common to all living things.
# - The 'Animal' class inherits from 'Organisom', so it gains its attributes.
# - The 'Dog' class inherits from 'Animal', thereby inheriting properties from both 'Animal' and 'Organisom'.


# Base Class: Organisom
class Organisom:
    # Class attribute: all organisms are considered alive.
    alive = True


# Intermediate Class: Animal
# Inherits from Organisom, so all Animal instances automatically have the 'alive' attribute.
class Animal(Organisom):
    def walk(self):
        # Method to simulate walking.
        print("This animal is walking.")


# Derived Class: Dog
# Inherits from Animal, gaining both the 'alive' attribute from Organisom and the walk() method from Animal.
class Dog(Animal):
    def bark(self):
        # Method specific to Dog to simulate barking.
        print("This dog is barking.")


# Creating an instance of Dog.
dog = Dog()

# Accessing the inherited 'alive' attribute from Organisom.
print(dog.alive)  # Output: True

# Calling the walk() method inherited from Animal.
dog.walk()  # Output: This animal is walking.

# Calling the bark() method defined in Dog.
dog.bark()  # Output: This dog is barking.

# Summary:
# - Multi-level inheritance forms a chain: Organisom -> Animal -> Dog.
# - The Dog class, as the most derived class, inherits attributes and methods from both its parent (Animal)
#   and grandparent (Organisom) classes.
# - This allows Dog to use the 'alive' attribute from Organisom, the walk() method from Animal, and its own bark() method.
# - Such inheritance structures promote code reuse and reflect real-world hierarchical relationships.
