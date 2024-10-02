### Generators
'''
def generate_even_nums(limit):
  num = 1
  my_list = []
  while num < limit:
    my_list.append(num*2)
    num = num + 1
  
  return my_list

'''
# The yield function generate a list of elements without consuming storage of the elements we don't use.
def generate_even_nums(limit):
  num = 1
  while num < limit:
    yield num * 2
    num = num + 1
  
even_numbers = generate_even_nums(6)

# I could print each number with a for loop
#for number in even_numbers:
#  print(number)

# I could print each number with the next clause
#print(next(even_numbers))
#print(next(even_numbers))
#print(next(even_numbers))

# when we write a * behind a parameter, we indicates that we are going to use an indeterminated amount of values.
"""
def return_cities(*cities):
	for e in cities:
		for se in e:
			yield se
"""
# The yield from clause allows eliminate the second for loop
def return_cities(*cities):
	for e in cities:
		yield from e


arg_cities = return_cities("Mar del Plata", "Mar del Tuyú", "Villa Gesell", "Cariló")

print(next(arg_cities))
print(next(arg_cities))