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
matrix = [['7','i','3'],['T', 's', 'i'], ['j', 's', 'i'], ['k', 's', 'p']]
hidden_message = []
number_of_col = len(matrix[0])
number_of_row = len(matrix)

for col_index in range(number_of_col):
    for row_index in range(number_of_row):
        current_character = matrix[row_index][col_index]
        if current_character.isalpha() == True:
            hidden_message.append(current_character)
        
        
        
        # print(matrix[row_index][col_index])

# for row_index in range(len(matrix)):
#     print(matrix[row_index][1])
    
# for row_index in range(len(matrix)):
#     print(matrix[row_index][2])

# print(matrix[0][0])
# print(matrix[1][0])
# print(matrix[2][0])