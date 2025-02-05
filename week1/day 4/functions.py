#Functions

#Syntax

def say_hello():
    print('Hello there!')

say_hello()

#Doc strings: explain the functions

def say_hello():
    '''prints a str 'Hello there!'''
    print('Hello there!')

say_hello()

#Passing information (arguments, parameters) into a function

def say_hello(username, language):
    if language == 'HE':
    print(f'Shalom, {username}!')
    elif language == 'RU':
    print(f'Private, {username}!')

say_hello('Harry')

#Exercise
#write a function called calculate_total that takes two arguments:
#price (a number) - the price of a single item
#quantity (a number) - the number of items
# print the total

def calculate_total(price_quantity):
    print('total: ', price * qauntity)

#Return - stops the code
def calculate_total(price, quantity)->int:
    return price * quantity

def fav_colors():
    fav_colors = ['blue', 'red', 'yellow']
    for color in fav_colors:
        return f'I love {color}]'
        print(f'I love {color}')

print(fav_colors())

#return multiple values

def get_country_info(country:str):
    if country == 'Israel':
        official_name = 'State of Israel'
        cpaital = 'Jerusalem'
        population = 100000
    
    elif country == 'Brazil'
    official_name = "Federative Republic of Brazil'
    capital =  'Brazilia'
    population = 216400000

else:
print('invalid country')

return offical_name, capital, population

#global and local scope

count_calculation = 100 #global scope

def calculation(a,b):
    addition = a + b 
    subtraction = a - b
    count_calculation += 1
    return addition, subtraction

print(calculation(8, 5, count_calculation))
print(count_calculation)

def welcome(clients:list):
    for client in clients:
        print(f'Welcome {client}')
        print(f'Welcome {client}')

welcome(clients)
print(clients)


         

