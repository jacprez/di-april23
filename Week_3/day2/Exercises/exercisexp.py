class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# 1. Create another cat breed named Siamese which inherits from the Cat class.

class Siamese(Cat):
    pass

# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.

all_cats =  [Bengal('Jonny', 1), Chartreux('Karly', 6), Siamese('Syd', 8)]
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
saras_pets = Pets(all_cats)
print(saras_pets)
# Take all the cats for a walk, use the walk method.

saras_pets.walk()


# 1. Create a class called Dog with the following attributes name, age, weight.

class Dog :
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        
    def bark(self):
        return f'{self.name} is barking'
    def run_speed(self):
        running_speed = self.weight / self.age * 10
        return running_speed
    def fight(self, other_dog):
        self_run_speed = self.run_speed() * self.weight
        other_run_speed = other_dog.run_speed() * other_dog.weight
        if self_run_speed > other_run_speed:
            return f'{self.name} won the fight.'
        elif self_run_speed < other_run_speed:
            return f'{other_dog.name} won the fight.'
        else:
            return 'It was a tie.'

# 3. Create 3 dogs and run them through your class.

dog1 = Dog("Kar", 3, 20)
dog2 = Dog("Syd", 5, 15)
dog3 = Dog("Steph", 2, 18)

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog3.fight(dog1))

# Exercise 3: Dogs Domesticated

from dogs import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        bark_output = self.bark()
        self.trained = True
        return bark_output

    def play(self, *args):
        dog_names = ', '.join(args)
        print(f"{dog_names} all play together.")

    def do_a_trick(self):
        if self.trained:
            trick_options = [
                f"{self.name} does a barrel roll.",
                f"{self.name} stands on his back legs.",
                f"{self.name} shakes your hand.",
                f"{self.name} plays dead."
            ]
            random_trick = random.choice(trick_options)
            print(random_trick)
        else:
            print(f"{self.name} is not trained yet.")

# Create instances of PetDog
pet_dog1 = PetDog("Max", 3, 20)
pet_dog2 = PetDog("Buddy", 5, 15)
pet_dog3 = PetDog("Cody", 4, 15)

# Train pet_dog1
print(pet_dog1.train())

# Play together
pet_dog1.play('Cody', 'Max', 'Buddy')
print()

# Do tricks
pet_dog1.do_a_trick()
pet_dog2.do_a_trick()
