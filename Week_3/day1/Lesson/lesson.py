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

class Dog :

    def __init__(self, name_dog, age_dog, dog_energy = 100) :
        self.name = name_dog
        self.age = age_dog
        self.energy =  dog_energy

    def bark(self):
        print(f"{self.name} said Wouaf Wouaf")

    def play(self, type_game="stick"):
        if self.energy < 10 :
            self.sleep()
        else : 
            if type_game == "ball":
                self.energy -= 10
            elif type_game == "stick":
                self.energy -= 5
            elif isinstance(type_game, Dog) :  #if its another dog then drop the energy of both dogs by 70
                print(f"{self.name} is playing with {type_game.name}")
                self.energy -= 70
                type_game.energy -= 50 #type_game is the other dog
            else :
                self.energy -= 2
    
    def play_with_other_dog(self, other_dog) :
        #other_dog is an object
        # print(other_dog.__dict__)
        print(f"{self.name} is playing with {other_dog.name}")
        self.energy -= 70
        other_dog.energy -= 50
    
    def sleep(self) :
        self.energy += 50

lea_dog = Dog("Rex", 4)
john_dog = Dog("Lola", 6, 200)
lea_dog.bark() #Rex said "Wouaf Wouaf"
john_dog.bark() #Lola said "Wouaf Wouaf"
lea_dog.play("ball")
print(lea_dog.energy)
lea_dog.play()
print(dir(lea_dog))
print(lea_dog.__dict__)

tom_dog = Dog("King", 7, 10)
print(f"the dog energy is {tom_dog.energy}")
tom_dog.play("ball")
print(f"the dog energy is {tom_dog.energy}")
tom_dog.play("ball")
print(f"the dog energy is {tom_dog.energy}")