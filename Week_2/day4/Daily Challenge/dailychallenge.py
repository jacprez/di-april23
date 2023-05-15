# Matrix

# reads each column from top to bottom, starting from the leftmost column, selecting only the alpha characters and connecting them. Then he replaces every group of symbols between two alpha characters by a space.

# matrix = """7i3
# Tsi
# h%x
# i #
# sM 
# $a 
# #t%
# ^r!"""
# matrix = [['7','i','3'],['T', 's', 'i'], ['#', 's', 'i'], ['^', 's', 'p']]
# hidden_message = []
# number_of_col = len(matrix[0])
# number_of_row = len(matrix)
# symbol_flag = False # This is to help flag situations of things to potentially remember. i.e. knowing if a character is a letter or symbol

# for col_index in range(number_of_col):
#     for row_index in range(number_of_row):
#         current_character = matrix[row_index][col_index]
#         if current_character.isalpha() == True:
#             if symbol_flag == True :
#                 hidden_message.append(" ")
#                 symbol_flag = False
#             hidden_message.append(current_character)
#         else:
#             symbol_flag = True
        
# print(hidden_message)
# print(''.join(hidden_message))
        
        # print(matrix[row_index][col_index])

# for row_index in range(len(matrix)):
#     print(matrix[row_index][1])
    
# for row_index in range(len(matrix)):
#     print(matrix[row_index][2])

# print(matrix[0][0])
# print(matrix[1][0])
# print(matrix[2][0])


# Class Way to do it


secret = """7i3
Tsi
h%x
i #
sM 
$a xs
#t%
^r!"""

def create_matrix () :
    lst_one = secret.split("\n")
    new_list = []
    for num in range(3) :
        new_list.append([char[num] for char in lst_one])
    # print(new_list)

    return new_list


def create_sentence() :
    lst = create_matrix() #"hello"
    sentence = ""
    for column in lst : 
        for char in column:
            if char.isalpha() :
                sentence += char
            else :
                sentence += " "

    print(sentence)

create_sentence()

