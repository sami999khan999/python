# The input() function in Python is used to read a line of text entered by the user. It returns the input as a string. This function allows programs to interact with users by receiving input dynamically.

name = input("What is you name? ")
age = int(input("How old are you? "))
height = float(input("How tall are you? "))

print("Hello," + name)
print("You are" +" " +str(age)+" "  + "years old.")
print("You are"+ " " +str(height) +" "+ "cm tall.")