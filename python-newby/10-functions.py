# Functions

def my_function():
    print("This is a function")

my_function()

def sum_two_values (first, second):
    print(int(first) + int(second))
sum_two_values (1, 2)

def multiply_to_values (first, second = 10): #The second value has a default value
    return first * second

print(multiply_to_values(3, 4))