# Functions
# Syntax
# def functionname () :
#     content of the function


# Variables created inside a function are called 'local variables' and variables created outside the function are called 'global variable'
# 'Global variables' can be used everywhere


# Create a function, that receives a number and checks if the number is even or odd

def even_odd (number) :
    if number % 2 == 0 :
        print(f'{number} is even')
    else:
        print(f'{number} is odd')
        
# Create a functions that receives a list of numbers, and check if each number is even or odd


