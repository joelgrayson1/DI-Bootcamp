# Ex1
def display_message():
    print('I am learning how to code using Python')

display_message()

#Ex2

def favorite_book(title):
    print(f'One of my favorite books is {title}')

favorite_book('Harry Potter')

#Ex3
def describe_city(city, country='Spain'):
    print(f'{city} is in {country}')


describe_city('Madrid', 'Spain')

describe_city('Madrid')

#Ex4

import random

def compare_numbers(user_number):
    random_number = random.randint(1, 100)
    
    if user_number == random_number:
        print('Success! The numbers match')
    else:
        print(f'Fail! The numbers do not match. Your number was {user_number}, and the random number was {random_number}.')

compare_numbers(50)

#Ex6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians():
    for magician in magician_names:
        print(magician)

def make_great():
    for i in range(len(magician_names)):
        magician_names[i] = magician_names[i] + ' the Great'

make_great()

show_magicians()

#Ex5

def make_shirt(size, message):
    print(f"The size of the shirt is {size} and the text is '{message}'")

make_shirt('Large', 'I Love Tel Aviv')

def make_shirt(size='Large', message='I love Python'):
    print(f"The size of the shirt is {size} and the text is '{message}'")

make_shirt()

make_shirt('Medium')

make_shirt('Small', 'I love Haifa')

#Ex7



