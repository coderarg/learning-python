# List Comprehension

# syntax
# [i for i in iterable if expression]


# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']


my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]

my_range = range(8)

my_list = [i for i in my_original_list]
print(my_list)

my_list = [i for i in range(8)]
print(my_list)

other_list = [i*2 for i in range(8)]
print(my_list)

def per_five(number):
    return number * 5

auto_sum_list = [per_five(i) for i in range(0, 5)]
print(auto_sum_list)