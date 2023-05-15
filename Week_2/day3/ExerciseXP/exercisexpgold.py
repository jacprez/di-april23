# Exercise 1: Concatenate Lists

# list_1 = [1,2,3,4,5]
# list_2 = [6,7,8,9,10]

# list_1.extend(list_2)
# print(list_1)

# Exercise 2: Range Of Numbers

# for number in range(1500,2500) :
#     if number % 5 ==0 or number % 7 == 0:
#         print(number)
        
# Exercise 3: Check The Index

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("What is your name? ")

if user_name in names :
        print(names.index(user_name))
        
