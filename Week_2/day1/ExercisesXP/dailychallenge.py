# Exercise 1

user_input = input("Write a word that is 10 characters long: ")

if len(user_input) < 10 :
    print(f"{user_input} is not long enough")
    user_input = input("Write a word that is 10 characters long: ")
elif len(user_input) > 10 :
    print(f"{user_input} is too long")
    user_input = input("Write a word that is 10 characters long: ")

# Exercise 2

user_answer = input("Write a word that is 10 characters long: ")

print(user_answer[0], user_answer[-1])

# Exercise 3

message = " "

word = "Hello World"
for char in word :
    message += char
    print(message)
    