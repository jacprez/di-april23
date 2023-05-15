# Everything in Python is an object
# Class is an object constructor or a "blueprint" for creating objects
# Each thing of object is an instance of a class
# An instance is a copy of the class with actual values 


# Create a Class

# Class is the template
class Car :
    # init function - constructor function
    # self means the object itself
    def __init__(self) :
        self.brand = "Ferrari" # Creating an attribute
        
        
my_car = Car()
# my_car is an instance of the class car
# my_car is an object


# Exercise 1
# Create a Employee class, With the attributes : firstname, lastname, age, job, salary
# Create 2 users object and display their attribute
# Lea Smith 30 years old developer 30000
# David Schartz 20 years old project manager 20000
# Add those methods to the class
# get_fullname(self) : that return the firstname + lastname
# happy_birthday(self) : that return the age incremented by one
# get_promotion(self, promotion_amount) : that increment the salary of the user by the promotion
# Call all the methods on the 2 objects


class Employee() :
    def __init__(self, firstname, lastname, age, job, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary
        
    def get_fullname(self):
        return self.firstname + " " + self.lastname
    def happy_birthday(self):
        self.age += 1
        return self.age
    def get_promotion(self, promotion_amount):
        self.salary += promotion_amount
        
lea = Employee('Lea', 'Smith', 30, 'Developer', 30000)

fn = lea.get_fullname()
print(fn)
# jackie_employee = Employee('Jackie', 'Prezant', 26, 'Student', 100000)
