# box contains attributes and methods
# attributes define an object


class Dog :
    # how you describe your dog should be in the init
    def __init__(self, color, breed, age):
        self.color = color
        self.breed = breed
        self.age = age
    
    def show(self):
        print(f"The dog is a {self.color} {self.breed}")
        
    def check_breed(self, best) :
        if self.breed == best :
            print('The dog is the best')
        else:
            print('The dog is not the best')
            
    def get_oldest_dog(self, other_dog) :
        print(other_dog.__dict__)
        if self.age > other_dog.age :
            print(f"{self.name} is taller than {other_dog.name}")

cody_dog = Dog('white', 'havanese')
zander_dog = Dog('brown', 'german shephard')

best_breed = 'havanese'

zander_dog.check_breed(best_breed) # --> The dog is not the best
cody_dog.check_breed(best_breed) # --> The dog is the best