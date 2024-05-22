# Higher Order Functions

def dummy_function(value):
    return value + 1

def sum_two_numbers_and_blablabla(first_value, second_value, super_important_function):
    print(super_important_function(first_value + second_value) )

#sum_two_numbers_and_blablabla(2,3, dummy_function)

# Built-in Higher Order Functions
# Map
numbers = [2, 5, 10, 21, 3, 40]

def multiply_by_two(num):
    return num * 2  

print(list(map(multiply_by_two, numbers)))
print(list(map(lambda X: X*2, numbers)))

# Filter
def filter_greater_than_ten(value):
    return value > 10

print(list(filter(filter_greater_than_ten,numbers)))
print(list(filter(lambda number: number > 10,numbers)))

# Reduce
# Reduce has been removed from Python 3.x.x. 
# So we need to import it from functools
from functools import reduce 

def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, numbers))
