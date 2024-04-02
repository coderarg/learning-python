# Classes

# Create a blank class
class BlankClass: 
    pass


class Person:
    def __init__(self, name, surname, alias = "Sin Alias"): #self is necessary to create a class
        # And alias has a default value
        self.name = name
        self.surname = surname
        self.alias = alias
        # private property
        self.__fullname = "Lucas García"
        """ The difference between common and private properties is that common properties, 
        unlike private properties, can be modified from outside the class."""

    # define a getter as a function
    def get_name (self):
        return self.__name
    
    # we can also define a function for this class
    def run (self):
        print(f"I´m {self.name} and I like running")
    def myAlias (self):
        print(f"My alias is {self.alias}")
    def myPrivateVariable(self):
        print(f"{self.__fullname}")


my_person = Person("Lucas", "García")
my_person.run()
my_person.myAlias()

other_person = Person("Brais", "Moure", "Mouredev")

other_person.myAlias()
other_person.myPrivateVariable()

