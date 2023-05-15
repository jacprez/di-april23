# Exercise 1: Cats

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
        

# cat_1 = Cat('Jimmy', 5)
# cat_2 = Cat('Ginger', 10)
# cat_3 = Cat('Fluffy', 14)

# def find_oldest(cats):
#     cat_ages = []
#     for cat in cats:
#         cat_ages.append(cat.age)
#     return max(cat_ages)


# print(find_oldest([cat_1, cat_2, cat_3]))

# Exercise 2 : Dogs


# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
        
#     def bark(self) :
#         print(f'{self.name} goes woof!')
        
#     def jump(self) :
#         jumping_height = self.height * 2
#         print(f'{self.name} jumps {jumping_height} cm high!')
        
        
# davids_dog = Dog('Rex', 50)

# print(davids_dog.name, davids_dog.height)

# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog('Teacup', 20)

# print(sarahs_dog.name, sarahs_dog.height)

# sarahs_dog.bark()
# sarahs_dog.jump()

# if davids_dog.height > sarahs_dog.height:
#     print(f'{davids_dog.name} is bigger than {sarahs_dog.name}')
# else:
#     print(f'{sarahs_dog.name} is bigger than {davids_dog.name}')



# Exercise 3 : Who’s The Song Producer?

class Song :
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(songs):
        for song in songs:
            print(song)
            

# Exercise 4 : Afternoon At The Zoo

