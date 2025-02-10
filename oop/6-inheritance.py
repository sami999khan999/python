# Inheritance allows a child class to use properties and methods from a parent class,
# promoting code reuse and hierarchical organization.


# Parent class: Animal
class Animal:
    # Initialize with name and age.
    def __init__(self, name, age):
        self.name = name  # Name of the animal.
        self.age = age  # Age of the animal.

    # Method to simulate eating.
    def eat(self):
        print(f"This {self.name} is {self.age} years old, and he is eating")

    # Method to simulate sleeping.
    def sleep(self):
        print(f"This {self.name} is {self.age} years old, and he is sleeping")


# Child class: Dog inherits from Animal.
class Dog(Animal):
    pass  # Inherits all attributes and methods from Animal.


# Child class: Cat inherits from Animal.
class Cat(Animal):
    pass  # Inherits all attributes and methods from Animal.


# Create instances of Dog and Cat.
dog = Dog("Dog", 9)  # Dog instance with name "Dog" and age 9.
dog.sleep()  # Uses the inherited sleep() method.

cat = Cat("Cat", 4)  # Cat instance with name "Cat" and age 4.
cat.eat()  # Uses the inherited eat() method.


# Summary:
# - Inheritance lets child classes (Dog, Cat) reuse code from a parent class (Animal).
# - Child classes automatically have the parent's attributes and methods.
# - The 'pass' statement indicates no extra functionality is added in the child classes.
