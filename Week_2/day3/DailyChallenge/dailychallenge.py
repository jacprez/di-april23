# Challenge 1


user_word = input("Please write a word: ")
indexes = {}

for i in range(len(user_word)) :
    letters = user_word[i]
    if letters in indexes :
        indexes[letters].append(i)
    else:
        indexes[letters] = [i]
        

print(indexes)

