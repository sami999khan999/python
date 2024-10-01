# Define a base class 'Animal'
# This class will serve as the "parent" class for all other animal types.
class Animal:

    # The constructor (__init__) method initializes the object with a name and age.
    def __init__(self, name, age):
        # 'self.name' and 'self.age' are instance variables unique to each object created.
        # These variables store the name and age of the animal.
        self.name = name
        self.age = age

    # Define a method called 'eat'.
    # This method can be used by any object of the 'Animal' class or any class that inherits from it.
    def eat(self):
        # Print the animal's name and age while they are eating.
        print(f"This {self.name} is {self.age} years old, and he is eating")

    # Define another method called 'sleep'.
    # Just like 'eat', this method can be used by any object of the 'Animal' class or its subclasses.
    def sleep(self):
        # Print the animal's name and age while they are sleeping.
        print(
            f"This {self.name} is {self.age} years old, and he is sleeping"
        )  # Fixed typo: 'sleepint' to 'sleeping'


# Define a subclass 'Dog' that inherits from the 'Animal' class.
# Inheritance allows 'Dog' to use methods and attributes from 'Animal' without redefining them.
class Dog(Animal):
    # The 'Dog' class doesn't define any new methods or attributes,
    # so it inherits everything from the 'Animal' class by default.
    # In this case, 'Dog' inherits the 'eat' and 'sleep' methods.
    pass  # The 'pass' statement is used when no additional code is required.


# Define another subclass 'Cat' that also inherits from the 'Animal' class.
class Cat(Animal):
    # The 'Cat' class also inherits all the attributes and methods from the 'Animal' class.
    # This means 'Cat' can also use the 'eat' and 'sleep' methods.
    pass


# Now let's create objects (instances) of the 'Dog' and 'Cat' classes.

# Create an instance of 'Dog'. The 'Dog' class doesn't need its own constructor because it inherits
# the constructor from 'Animal'. Here, the dog's name is "Dog" and its age is 9.
dog = Dog("Dog", 9)

# Call the 'sleep' method for 'dog'. Since 'Dog' inherits from 'Animal', it uses the 'sleep' method from 'Animal'.
# Output: "This Dog is 9 years old, and he is sleeping"
dog.sleep()

# Create an instance of 'Cat'. Like 'Dog', 'Cat' uses the constructor inherited from 'Animal'.
# The cat's name is "Cat" and its age is 4.
cat = Cat("Cat", 4)

# Call the 'eat' method for 'cat'. Since 'Cat' inherits from 'Animal', it uses the 'eat' method from 'Animal'.
# Output: "This Cat is 4 years old, and he is eating"
cat.eat()
