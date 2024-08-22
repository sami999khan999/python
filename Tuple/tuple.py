# tuple

# A tuple is an immutable, ordered collection of items in Python. Like lists, tuples can store elements of different data types, but unlike lists, tuples cannot be modified after they are created. Tuples are often used to represent fixed collections of items that should not change.

my_tuple = (1, 4, 2, 8, 4, 0)

print(my_tuple)

# ===================================================================================================== #

mixed_tuple = ("apple", 1, [2, 3, 4], True, "apple", 1, 2)

print(mixed_tuple)
print(mixed_tuple.count("apple"))
print(mixed_tuple[0])
print(mixed_tuple[-1])
print(mixed_tuple.index("apple"))

for i in mixed_tuple:
    print(i)

if "apple" in mixed_tuple:
    print("apple is here!")
