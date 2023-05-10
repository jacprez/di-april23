# Exercise 1 : What are you learning?

# def display_message(*args) :
#     argument = str(args)
#     print(f"I am learning {argument}")
    
    
# display_message('Python,', 'Javascript')


# OR

# def display_message(lesson):
#     print(f"I am learning {lesson}")
    
# display_message("python")


# Exercise 2: What’s Your Favorite Book ?

# def favorite_book(title) :
#     print(f'One of my favorite books is {title}')
    
# favorite_book('Harry Potter')


# Exercise 3 : Some Geography

# def describe_city(city = 'New York', country = 'USA') :
#     print(f'{city} is in {country}')
    
# describe_city('London', 'England')

# Exercise 4 : Random

# import random

# def compare_numbers(num) :
#     random_num = random.randint(1,100)
    
#     if num == random_num :
#         print(f'Awesome! The number is {num}')
#     else:
#         print(f'Not good. The random number is {random_num} and you entered {num}')
        
# compare_numbers(52)

# Exercise 5 : Let’s Create Some Personalized Shirts !

# def make_shirt(size = 'large', message = 'I love Python'):
#     print(f'The size of your shirt is {size} with the messaging {message}.')

# # 5. Make a large shirt with the default message
# make_shirt()

# # 6. Make medium shirt with the default message
# make_shirt('medium')

# #7 Make a shirt of any size with a different message.
# make_shirt('Small', 'Python is harder than I thought')

# Exercise 6: Magicians

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']



# def show_magicians(magicians):
#     for magician in magicians :
#         print(magician)
        
        
# def make_great(magicians):
#     for index in range(len(magicians)) :
#         magicians[index] += " the Great"
    
    
# make_great(magician_names)
# show_magicians(magician_names)


# Exercise 7 : Temperature Advice

import random

# def get_random_temp() :
#     return random.randint(-10, 40)

# print(get_random_temp())

# 3
# def main() :
#     random_temp_number = get_random_temp()
#     if random_temp_number < 0 :
#         print(f"The temperate right now is {random_temp_number} degrees which is below 0.")
#     elif 0 < random_temp_number < 16 :
#         print(f"Quite chill! Don't forget your coat.")
#     elif 16 < random_temp_number < 23 :
#         print(f"It is {random_temp_number} degrees outside")
#     elif 23 < random_temp_number < 40 :
#         print(f"It's pretty hot out there.")
    
    
# main()

# 4

def get_random_temp(season) :
    return random.randint(-10, 40)