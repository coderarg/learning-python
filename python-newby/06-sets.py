# Sets
# Group of unordered unique elements

my_set = set()
print(type(my_set))
other_set = {} # => Dictionary
print(type(other_set))

other_set = {"Brais", "Moure", 35}
print(type(other_set)) # => Set

# Length
print(len(other_set))

# We can't select item by index
# other_set[1] # => ERROR

# Add an element at first position
other_set.add("MoureDev")
other_set.add("MoureDev") #Nothing happens, cause sets doesn't admit duplicates

# Exist?
print("Moure" in other_set)
print("Mouri" in other_set)

# Remove an element
other_set.remove("Moure")
print(other_set)

# Remove all elements
other_set.clear()

# Delete set
del other_set

set_1 = {1, 3, 5}
set_2 = {2, 4, 5}

union_set = set_1.union(set_2)
print(union_set)

difference_set = set_2.difference(set_1)
print(difference_set)