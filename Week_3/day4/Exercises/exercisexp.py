# Exercise 1 – Random Sentence Generator

# with open('Week_3/day4/Exercises/sowpods.txt', 'r') as word_list:
#     pass

#     for word in word_list:
#         if word[0] == 'A':
#             print(word)
            
import random
            
def get_words_from_file(file_path):
    with open(file_path, 'r') as word_file:
        content = word_file.read()
        word_list = content.split()
        return word_list #will store in a list

file_name = 'Week_3/day4/Exercises/sowpods.txt'

words_list = get_words_from_file(file_name)

def get_random_sentence(list):
    length_of_sentence = int(input("How long should the sentence be? "))
    random_list = random.choices(list, k=length_of_sentence)
    return random_list
        
        
sentence_list = get_random_sentence(words_list)
sentence_string = ' '.join([str(word) for word in sentence_list])
print(sentence_string.lower())