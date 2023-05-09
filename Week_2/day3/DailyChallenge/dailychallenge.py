# Challenge 1


# user_word = input("Please write a word: ")
# indexes = {}

# for i in range(len(user_word)) :
#     letters = user_word[i]
#     if letters in indexes :
#         indexes[letters].append(i)
#     else:
#         indexes[letters] = [i]
        

# print(indexes)

# Challenge 2



# items_purchase = [{
#     'apple' : 22 ,
#     'shoes' : 200 ,
#     'berries' : 60 ,
#     'pan' : 250,
#     'computer' : 500
#  }]

# wallet = 550
# can_afford = []


# for item in items_purchase :
#     print(item)


    # if price <= wallet :
    #     can_afford.append(item)
    #     # wallet -= item


# print(can_afford)





# Define the wallet balance
wallet_balance = 50.0

# Define a list of store items with prices
store_items = [("apple", 1.0), ("banana", 0.5), ("cherry", 2.0), ("date", 1.5)]

# Create an empty list to store affordable items
affordable_items = []

# Iterate over each store item and check if it can be afforded
for item, price in store_items:
    if price <= wallet_balance:
        affordable_items.append(item)

# Sort the affordable items in alphabetical order
affordable_items.sort()

# Print the list of affordable items or "Nothing" if there are none
if affordable_items:
    print("Affordable items:", affordable_items)
else:
    print("Nothing")
