# scope = In Python, scope refers to the region of a program where a particular variable or function is accessible. It defines the visibility and lifetime of a variable. Variables can have local, enclosing, global, or built-in scopes, depending on where they are declared and used. Python follows the LEGB rule to determine the scope of a variable, which stands for Local, Enclosing, Global, and Built-in.

name = "sami"  # global scope (available inside and outside of any function)


def greet():
    name = "khan"  # locale scope (available only inside this fucntion)
    print(name)


greet()
print(name)
