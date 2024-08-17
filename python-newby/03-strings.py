"""
# Strings
my_string  = "Mi String"
my_other_string = 'Mi otro String'
print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)
my_new_line_string = "Es es un string \ncon salto de linea"
print(my_new_line_string)
my_tab_string = "Es es un string \tcon salto de tabulación"
print(my_tab_string)

#Format a string

name, surname, age = "Lucas", "García", 27

# Estas opciones de concatenación de strings es mucho más performante...
print("Mi nombre es {} {} y tengo {} años".format(name, surname, str(age)))
print("Mi nombre es %s %s y tengo %d años" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y tengo {age} años")

#... que la siguiente manera.
print("Mi nombre es " + name + " " + surname + " y tengo " + str(age) + " años.")

# Slice
language = "python"

print(language[0:3])
print(language[2:])
print(language[-3])

# Reverse
print(language[::-1])

# Capitalize
print(language.capitalize())

# Upper
print(language.upper())

# Lower
print(language.lower())

# Count letter
print(language.count('t'))

# isnumeric
print("1".isnumeric()) #true

# starts with
print("Hi".startswith("H")) #true

# Trim a string
#For whitespace on both sides, use str.strip():
s = "  \t a string example\t  "
s = s.strip()

#For whitespace on the right side, use str.rstrip():
s = s.rstrip()

#For whitespace on the left side, use str.lstrip():
s = s.lstrip()

#You can provide an argument to strip arbitrary characters to any of these functions, like this:
s = s.strip(' \t\n\r')
"""

