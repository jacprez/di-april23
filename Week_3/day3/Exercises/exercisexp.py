# Exercise 1 : Built-In Functions

# def __abs__(number):
#     return number

# def __int__(number):
#     return number


def my_abs(arg:int):
    ''' abs() is a built-in functions that returns the absolute value'''
    
    print(abs(arg))
    
my_abs(-123)
print(my_abs.__doc__)

# Exercise 2: Currencies

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
        
    def __str__(self):
        if self.amount > 1:
            return str(f"{self.amount} {self.currency}s")
        else:
            return str(f"{self.amount} {self.currency}")
            
    def __int__(self):
        return int(self.amount)
    
    def __repr__(self):
        if self.amount > 1:
            return str(f"{self.amount} {self.currency}s")
        else:
            return str(f"{self.amount} {self.currency}")
            
    def __add__(self, num):
        if self.currency != num.currency :
            print("ERROR")
        else:
            return self.amount + num
        # this part isn't working and I can't figure out how to solve it
c1 = Currency('dollar', 5)
print(str(c1))

print(int(c1))

print(repr(c1))

print(c1 + 5)