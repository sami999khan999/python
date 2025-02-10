# Duck Typing in Python:
# Duck typing is a programming concept where an object's suitability is determined by the presence
# of certain methods and properties, rather than the actual type of the object.
# In other words, if an object "quacks" (implements the required methods), it can be used in place of another,
# regardless of its class. This approach promotes flexibility and code reuse.


# Define a Duck class with the expected behaviors.
class Duck:
    name = "Duck"  # Class attribute shared by all Duck instances.

    def walk(self):
        # This method shows that a Duck can "walk".
        print(f"This {self.name} is walking.")

    def talk(self):
        # This method shows that a Duck can "talk" (quack).
        print(f"This {self.name} is quacking.")

    def __repr__(self):
        return f"This is a {self.name}"


# Define a Chicken class with similar behaviors.
class Chicken:
    name = "Chicken"  # Class attribute shared by all Chicken instances.

    def walk(self):
        # Chicken also implements a walk method.
        print(f"This {self.name} is walking.")

    def talk(self):
        # Chicken's talk method demonstrates it can "talk" (cluck).
        print(f"This {self.name} is clucking.")

    def __repr__(self):
        return f"This is a {self.name}"


# The Person class demonstrates duck typing.
# It doesn't care about the object's type; it only expects the object to have 'talk' and 'walk' methods.
class Person:
    def catch(self, bird):
        # Here, 'bird' can be any object that implements the methods 'talk' and 'walk'.
        # No type checking is performed; this is the essence of duck typing.
        # bird.talk()  # Call the object's talk method.
        # bird.walk()  # Call the object's walk method.
        print(bird)


# Create instances of Duck and Chicken.
duck = Duck()  # Instance of Duck.
chicken = Chicken()  # Instance of Chicken.

# Create an instance of Person.
person = Person()

# Demonstrate duck typing:
# The Person's catch method works with any object that implements 'talk' and 'walk', regardless of its class.
print("Using duck:")
person.catch(duck)
# Expected Output:
# "This Duck is quacking."
# "This Duck is walking."

print("\nUsing chicken:")
person.catch(chicken)
# Expected Output:
# "This Chicken is clucking."
# "This Chicken is walking."

# Additional Explanation:
# - The Person class does not check the type of the 'bird' parameter.
#   It simply assumes that the object passed in has the required methods.
# - This flexibility allows us to use different types of objects interchangeably, as long as they implement the expected behavior (in this case, talk and walk).
# - Duck typing emphasizes "behavior" over "type" - it's not important what an object is, but what it can do.
# - This makes Python code very flexible and easy to extend, as new classes can be integrated seamlessly
#   if they implement the expected interface, even without inheriting from a common parent class.

# Summary:
# - Duck typing focuses on the methods an object has, rather than its class type.
# - If an object implements the necessary methods (like 'talk' and 'walk'), it can be used in any context
#   that requires those methods.
# - This approach allows for greater flexibility and code reuse in Python.
