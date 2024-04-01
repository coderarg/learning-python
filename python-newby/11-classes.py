# Classes

# Create a blank class
class BlankClass: 
    pass


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

my_person = Person("Lucas", "García")
print(my_person.name)

