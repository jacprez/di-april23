# Exercise 1
# Create a Employee class, With the attributes : firstname, lastname, age, job, salary
# Create 2 users object and display their attribute
# Lea Smith 30 years old developer 30000
# David Schartz 20 years old teacher 15000
# Add those methods to the class
# get_fullname(self) : that return the firstname + lastname
# happy_birthday(self) : that return the age incremented by one
# get_promotion(self, promotion_amount) : that increment the salary of the user by the promotion

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

# implement the gt dunder method that receives 2 different employees, and returns the employee with the highest salary
    def __gt__(self, other):
        if self.salary > other.salary:
            return self.firstname
        else:
            return other.firstname
# implement the add dunder method that that receives 2 different employees, and returns the total salary of the 2 employees
    def __add__(self, other):
        return self.salary + other.salary
# implement the str dunder method that introduce the employee
    def __str__(self):
        return f"The Employee: {self.firstname} {self.lastname} is a {self.age} years old {self.job} and makes {self.salary} dollars a year."
# Call all the methods

first_employee = Employee('Jackie', 'Prezant', 26, 'Developer', 150000)
second_employee = Employee('Jonathan', 'Prez', 31, 'Therapist', 75000)

print(first_employee > second_employee)
print(first_employee)


# Static Methods
# Decorator decorates a function - gives it more features without changing the functions - not changing but adding more to it 

# example: @staticmethod