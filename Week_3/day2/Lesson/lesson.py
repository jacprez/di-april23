# Inheritance
class Dog :

    def __init__(self, name_dog, age_dog, dog_energy = 100) :
        self.name = name_dog
        self.age = age_dog
        self.energy =  dog_energy

    def bark(self):
        print(f"{self.name} said Wouaf Wouaf")
    
    def is_happy(self, mood) :
        print(f"The dog is {mood}")

# inheritance
# child receives from the parents - doesnt give anything back
class GermanShepard(Dog):

    def __init__(self, dog_name, dog_age, dog_color, dog_energy = 200) :
        super().__init__(dog_name, dog_age, dog_energy) #init from the parent
        self.color = dog_color
    
    def jump(self) :
        print(f"{self.name} jumps high")
    
    # override
    def bark(self):
        print(f"{self.name} said Wouaf Wouaf I'm a strong german shepard")

    def is_happy(self, mood) :
        super().is_happy(mood) # call the parent method
        print("Of course he is a german shepard")


my_dog = GermanShepard("Rex", 12, "brown")
# print(dir(my_dog))
# my_dog.bark()
my_dog.jump()
my_dog.bark()
my_dog.is_happy("joyful")
print(my_dog.__dict__)

other_dog = Dog("Lola", 10)
# other_dog.jump() # not possible because the jump method
# is only accessible from the GermanShepard
# meaning only german shepard can jump - not all dogs











class Employee :
    def __init__(self, emp_fn, emp_ln, emp_age, emp_job, emp_salary) :
        self.firstname = emp_fn
        self.lastname = emp_ln
        self.age = emp_age
        self.job = emp_job
        self.salary = emp_salary

    def get_fullname(self) :
        fullname = self.firstname + " " + self.lastname
        return fullname
    
    def happy_birthday(self) : 
        self.age += 1
    
    def get_promotion(self, promotion_amount) :
        self.salary += promotion_amount

    def show_employee(self) :
        print(f"{self.firstname} {self.lastname} {self.age} {self.job} {self.salary}")
        
class Developer(Employee):
    def __init__(self, emp_fn, emp_ln, emp_age, emp_job, emp_salary):
        super().__init__(emp_fn, emp_ln, emp_age, emp_job, emp_salary)