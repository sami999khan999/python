# slice object

# The slice object in Python is a built-in tool that allows you to define a slice of a sequence without directly slicing it. You can create a slice object with start, stop, and step parameters and then apply it to a sequence (like a list, tuple, or string).

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

website1_name = website1[slice]
website2_name = website2[slice]

print(website1_name)
print(website2_name)