# set methods

my_set = {1, 2, 3, 4, 5}

print(my_set)

# ===================================================================================================== #

# add

# Adds an element to the set

my_set.add(5)

print(my_set)

# ===================================================================================================== #

# remove

# Removes the specified element from the set. Raises a KeyError if the element is not found.

my_set.remove(1)

print(my_set)

# ===================================================================================================== #

# discard

# Removes the specified element from the set if it exists. Does not raise an error if the element is not found.

my_set.discard(2)

print(my_set)

# ===================================================================================================== #

# pop

# Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.

my_set.pop()

print(my_set)

# ===================================================================================================== #

# clear

# Removes all elements from the set.

my_set.clear()

print(my_set)

# ===================================================================================================== #

# update

# Adds multiple elements to the set. You can pass any iterable (e.g., list, tuple, another set) to this method, and it will add all unique elements from that iterable to the set.

set_1 = {1, 3, 5, 7}
set_2 = {2, 4, 6, 8}

set_1.update(set_2)

print(set_1)

# ===================================================================================================== #

# union

# Returns a set containing all elements from both sets.

even_num = {2, 4, 6, 8}
odd_num = {1, 3, 5, 7}

union_set = even_num.union(odd_num)
nuion_set_2 = even_num | odd_num

print(union_set)
print(nuion_set_2)

# ===================================================================================================== #

# intersection

# Returns a set containing only the elements that are present in both sets.

set_3 = {2, 4, 6, 8, 10}
set_4 = {4, 8, 12, 16, 20}

intersection_set = set_3.intersection(set_4)
intersection_set_2 = set_3 & set_4

print(intersection_set)
print(intersection_set_2)

# ===================================================================================================== #

# difference

# Returns a set containing all elements that are in the first set but not in the second set.

set_5 = {1, 2, 3, 4, 5}
set_6 = {1, 5, 7, 0, 8}

difference_set = set_5.difference(set_6)
difference_set_2 = set_5 - set_6

print(difference_set)
