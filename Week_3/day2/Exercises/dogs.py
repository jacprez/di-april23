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