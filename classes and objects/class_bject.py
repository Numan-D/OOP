#CLASSES AND OBJECTS#

"""This code is built aimed at allowing the user to submi their details about their car via the OOP programming"""


#this part defines the data then uses it later on.
class Car:
    def __init__(self, brand, type, colour, year):
        self.brand = brand
        self.type = type
        self.colour = colour
        self.year = year

    def sentence(self):
        return f"Hi, my vehicle is a {self.brand}, which is a {self.type} and is the colour {self.colour} and is a {self.year} model"

    def get_brand(self):
        return self.brand

    def get_type(self):
        return self.type

    def get_colour(self):
        return self.colour
        
    def get_year(self):
        return self.year

    

# Creating objects (instances)
car1 = Car("Volvo", "sedan", "red", 2019)
car2 = Car("Toyota", "hatchback", "blue", 2020)


#this is the command that calls the relevent information#
print(car2.sentence())