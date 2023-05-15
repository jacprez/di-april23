# Instructions : Old MacDonald’s Farm

class Farm :
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.all_animals = {}
    
    def add_animal(self, animal_name, amount = 1):
        if animal_name in self.all_animals:
            self.all_animals[animal_name] += amount
        else:
            self.all_animals[animal_name] = amount
            
    def get_info(self):
        print(f"{self.farm_name}'s Farm \n")
        for animal, amount in self.all_animals.items() :
            print(f'{animal} :{amount}')
        print("       E-I-E-I-O")
        
    def get_animal_types(self) :
        all_keys = list(self.all_animals.keys())
        return sorted(all_keys)
    
    def get_short_info(self):
        all_animal_keys = self.get_animal_types()
        for animal, amount in self.all_animals.items() :
            if amount > 1 :
                position_animal = all_animal_keys.index(animal)
                all_animal_keys[position_animal] += 's'
        joining_animals = ", ".join(all_animal_keys[:-1])
        sentence = f"\n{self.farm_name} Farm has {joining_animals} and {all_animal_keys[-1]}"
        print(all_animal_keys)
        
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_animal_types())
macdonald.get_short_info()