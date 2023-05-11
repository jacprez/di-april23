def loop_over_values(**person):
    print(person)


loop_over_values(name = 'Jackie', age = 26, citizen = "USA and IL") # This will produce a dictionary
   
# Output: {'name': 'Jackie', 'age': 26, 'citizen': 'USA and IL'}

# **kwargs pack the values into a dictionary