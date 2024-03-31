# Functions

def my_function():
    print("This is a function")

my_function()

def sum_two_values (first, second):
    print(int(first) + int(second))
sum_two_values (1, 2)

def multiply_two_values (first, second = 10): #The second value has a default value
    return first * second

print(multiply_two_values(3, 4))

def multiply_each_number (*numbers): # Apply the function to each element
    product = 0
    for number in numbers:
        if product == 0: product = number
        else: product *= number
    
    return product

print(multiply_each_number(1, 3, 3, 3))

