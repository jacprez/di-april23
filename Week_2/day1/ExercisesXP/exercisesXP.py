#Exercise 1 : Hello World

print("Hello World\n" * 4)


#  Exercise 2 : Some Math

print(pow(99, 3) * 8)

# Exercise 3 : What Is The Output ?

5 < 3       # False
3 == 3      # True
3 == "3"    # False
"3" > 3     # Error
"Hello" == "hello"  #False

# Exercise 4 : Your Computer Brand

computer_brand = "MacBook"
print(f"I have a {computer_brand} computer")


# Exercise 5 : Your Information

name = "Jackie"
age = 26
shoe_size = 40
info = f"My name is {name}. I am {26} years old and have a size {shoe_size}."
print(info)

# Exercise 6 : A & B

a = 10
b = 5

if a > b :
    print("Hello World")
    
# Exercise 7 : Odd Or Even 

num = int(input("Enter a number to see if it's odd or even: "))

if (num % 2) == 0 :
    print(f"{num} is even")
else :
    print(f"{num} is odd.")
    
# Exercise 8 : What’s Your Name ?

my_name = "Jackie"
user_name = input("What is your name? ")

if user_name == my_name :
    print("We have the same name!")
elif user_name != my_name :
    print("We don't have the same name!")
    

# Exercise 9 : Tall Enough To Ride A Roller Coaster

height = int(input("How tall are you? "))

if height > 145 :
    print("You can ride.")
else :
    print("You can't ride.")