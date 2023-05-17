# Bankerrors

class BankAccount :
    def __init__(self, amount, name):
        self.amount = amount
        self.name_holder = name
        
    def withdraw(self, amount_to_withdraw):
        try : # the try should contan the code that might contain an error
            if type(amount_to_withdraw) != int:
                raise TypeError("Wrong data")
            
            if amount_to_withdraw < self.amount:
                print('Your withdrawal was successful')
                raise ValueError("You don't have enough")
            else: 
                raise ValueError("Not enough money")
        except Exception as error:
            # pass
            print(error)
            
            
# Create a colorize(text, color) function that contain this tuple 
# colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')

# If the color is not present in the tuple, raise a ValueError exception
# If the text is not a string raise a TypeError Exception
# make sure to catch the exception
# colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
# def colorize(text, color) :
#     colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
#     try:
#         if type(text) != str:
#             raise TypeError(f"{text} is not a string")
        
#         if color not in colors:
#                 raise ValueError(f"{color} is not in the list")
#         elif text not in colors:
#                 raise ValueError(f"{text} not in colors")
#         else:
#                 print('Everything looks good')
#     except Exception as error:
#         print(error)
        
# colorize("hello", "cyan")

def colorize(text, color):
    colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
    try:
        if type(text) != str:
            raise TypeError("The input is not a string")
        elif color not in colors:
            raise ValueError("color is not in tuple")
    except ValueError as error1:
        print("Value Error")
        print(error1)
    except TypeError as error2:
        print("Type Error")
        print(error2)
        
    print("end of function")

colorize("hello", "cyan")
colorize(123, "red")
colorize("hello", "red")