
# colors.insert(2, "white") # ["blue", "red", "white", "pink"]
# colors = ["blue", "red", "pink"]
# user_answer = input("Give me a position and a color: ")

# answer_list = user_answer.split(",")
# x = int(answer_list[0])
# y = answer_list[1]
# colors.insert(x,y)
# print(colors)


# colors = ["blue", "red", "pink"]
# colors.pop() # delete last element
# print(colors)

# Platform Exercise

# list1 = [5, 10, 15, 20, 25, 50, 20]
# index_of_20 = list1.index(20)
# list1[index_of_20] = 200

# print(list1)



# Loops

# list(range(5)) # [0, 1, 2, 3, 4] (5 is not included since we start at 0)

# colors = ["blue", "red", "yellow", "pink"]

# for color in colors :
#     print(color)
    
numbers = [1,2,3,4,5,6]

for num in numbers :
    if num % 2 ==0 :
        print(f"the number {num} is even")
    else :
        print(f"the number {num} is odd")