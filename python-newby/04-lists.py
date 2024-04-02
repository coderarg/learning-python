# Lists

my_list = list()
my_list = [35, 7, 5, 87, 5, 54]

other_list = ["Lucas", "garcia", 1.74, 27]

print(len(my_list))
print(other_list[0]) #first element
print(other_list[1]) #second element
print(other_list[-1]) #last element
print(other_list[-3])
# print(other_list[-5]) # IndexError

# Count
print(my_list.count(5))
# Index
other_list.index("Lucas")

# Append
my_list.append("Elemento")

# Insert
my_list.insert(1, "Elemento")

# Remove the first it finds
my_list.remove("Elemento")

# Delete element by index
del my_list[2]

# Pop by default, delete de last element and returns it
pop_element = my_list.pop()
# Also, we could extract a selected element from the list using the index
pop_selected = my_list.pop(3)

# Reasign a value
my_list[0] = 27
other_list[1] = "García"

# Copy list into another list
my_second_list = my_list.copy()

# Reverse de order of the list
my_second_list.reverse()

# Sort a list
my_second_list.sort()
print(my_second_list)
my_second_list.sort(reverse= True)
print(my_second_list)

# Creat a sorted list
sorted_list = sorted(my_list)

# Remove all list elements
my_list.clear()
