# Exercise 1 : Set 

# my_fav_numbers = {6, 10, 63, 12}

# # my_fav_numbers.update([1, 2])

# # print(my_fav_numbers)

# # my_fav_numbers.pop()

# # print(my_fav_numbers)

# friend_fav_numbers = {2, 4, 8, 22, 46, 84}

# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

# Exercise 2: Tuple

# You cannot add or remove items from a tuple after it has been created. Tuples are ordered, unchangeable and can have duplicates

# Exercise 3: List

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# basket.remove("Banana")
# print(basket)
# basket.remove("Blueberries")
# print(basket)
# basket.append("Kiwi")
# print(basket)
# basket.insert(0, "Apples")
# print(basket)
# number_of_apples = basket.count("Apples")
# print(number_of_apples)
# basket.clear()
# print(basket)

# Exercise 4: Floats

#Float: decimal point number - "floating-point number"
#Float is a deimal number and an integer is a whole number

# dec_list = []

# for num in range(11):
#     dec = num / 10.0
#     dec_list.append(dec)
    
# print(dec_list)

# float_list = []
# for num in range(3, 11, 1) :
#     dec = num / 2
#     float_list.append(dec)

# print(float_list)
    
# Exercise 5: For Loop

# for num in range(1,21) :
#     print(num)

# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

# Exercise 6 : While Loop

# user_name = input("What is your name? ")
# my_name = "Jackie"

# while user_name != my_name :
#     user_name = input("What is your name? ")
    
# print("You guessed it right!")

# Exercise 7: Favorite Fruits

# favorite_fruits = input("Please share your favorite fruits and separate the fruits with a single space: ")

# favorite_fruits_list = favorite_fruits.split(" ")
# print(favorite_fruits_list)

# for fruit in favorite_fruits_list :
#     user_fruit = input("What is your favorite fruit? ")
#     if user_fruit in favorite_fruits_list :
#         print("You chose one of your favorite fruits!")
#     else:
#         print("You chose a new fruit. Enjoy!")
#     break

# Exercise 8: Who Ordered A Pizza ?

user_answer = ""
all_toppings = []

while user_answer != "quit" :
    print(f"We will add {user_answer} to your pizza")
    all_toppings.append(user_answer)
    user_answer = input("Give me a pizza topping ")
print("this is your pizza toppings")

