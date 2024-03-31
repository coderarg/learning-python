# Dictionaries

my_dict = dict()
other_dict = {}

other_dict = {"Name": "Brais", "Surname": "Moure", "Age": 35}

my_dict = {
    "Name": "Brais", 
    "Surname": "Moure", 
    "Age": 35,
    "Languages": {"Python", "JavaScript", "C#"},
    1: "Number"
}

# Access to an attribute
print(my_dict["Name"])
print(my_dict[1])

# Update an attribute
my_dict["Name"] = "Lucas"

# Add a key-value
my_dict["Location"] = "Av Siempre Viva 1234"

print(my_dict)

# Delete an element
del my_dict["Location"]

# Find a key
"Surname" in my_dict
1 in my_dict

# Elements
print(my_dict.items()) # Returns all
print(my_dict.keys()) # Returns keys
print(my_dict.values()) # Returns values

# New dictionary without values
my_new_dict = dict.fromkeys(("Name", "Surname", "Age"))
print(my_new_dict)

# New dictionary with default values
my_second_dictionary = dict.fromkeys(["Name", "Surname"], "something")
print(my_second_dictionary)

#test list of dictionaries
my_dict_list = [
    {
        "Name": "Lucas",
        "Surname": "García"
    },{
        "Name": "Fabiola",
        "Surname": "Linares"
    }
]

my_dict_list.append({
    "Name": "Gustavo",
    "Surname": "Gonzalez"
})

for elem in my_dict_list:
    print(elem["Name"])