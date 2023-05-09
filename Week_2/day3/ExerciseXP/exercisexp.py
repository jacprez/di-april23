# Exercise 1 : Convert Lists Into Dictionaries

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# new_dict = zip(keys, values)

# print(dict(new_dict))

# Exercise 2 : Cinemax

# family = {
#     "rick" : 43 ,
#     'beth' : 13 ,
#     'morty' : 5 ,
#     'summer' : 8 ,
# }

# family_ages = list(family.values())
# print(family_ages)

# price_to_pay = 0

# for num in family_ages :

#     if  > 3 :
#         print('Your ticket is free')
#     elif 12 > num > 3 :
#         print('Your ticket costs $10')
#         price_to_pay += 10
#     else:
#         print('Your ticket costs $15.')
#         price_to_pay += 15
    
# print(f'Your total is {price_to_pay}')
    
# Exercise 3: Zara

brand = { 
            'name' : 'Zara' ,
            'creation_date': '1975' ,
            'creator_name': 'Amancio Ortega Gaona ',
            'type_of_clothes': ['men', 'women', 'children', 'home'] ,
            'international_competitors':[ 'Gap', 'H&M', 'Benetton' ] ,
            'number_stores': 7000 ,
            'major_color': {
                'France': 'blue', 
                'Spain': 'red', 
                'US': ['pink', 'green' ]
            }
}

brand['number_stores'] = 2
print(brand['number_stores'])

brand['country_creation'] = 'Spain'
print(brand)

if 'international_competitors' in brand :
    brand['international_competitors'].append('Desigual')

print(brand['international_competitors'])

del brand['creation_date']
print(brand)

# Print the last international competitor.

# last_comp = brand['international_competitors'][-1]

# print(last_comp)

# Print the major clothes colors in the US.

# colors = brand['major_color'].values()

# print(colors)

# Print the major clothes colors in the US.

# print(len(brand))

# Print the keys of the dictionary.

print(brand.keys())

more_on_zara = dict({
    'creation_date' : 1975 ,
    'number_stores' : 10000
})

brand['more_on_zara'] = brand

print(brand['more_on_zara']) # added an empty dictionary