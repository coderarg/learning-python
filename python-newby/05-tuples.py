# Tuples

my_tuple = tuple()
my_other_tuple = (88, 33, 44)

my_tuple = (27, 1.74, "Lucas", "García")
print(my_tuple)
print(type(my_tuple))

# Returns a selected element
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[-3])

# Count a value
my_tuple.count(27) # Returns count
my_tuple.index("García") # Returns index

# Tuples are immutable: We can't change a value of the tuple
# my_tuple[0] = 30 -> Error

# Sum tuples
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# We can change the type of the element tuple to list
list_from_tuple = list(my_tuple)
print(type(list_from_tuple))

# And come back to a tuple
tuple_from_list = tuple(list_from_tuple)

# We can´t delete a selected element
#del my_tuple[1] -> Error

# Del the tuple
del my_tuple