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

def get_random_temp(season):
    if season == 'winter':
        return round(random.uniform(-10, 16), 1)
    elif season == 'spring':
        return round(random.uniform(0, 20), 1)
    elif season == 'summer':
        return round(random.uniform(16, 40), 1)
    elif season == 'autumn' or season == 'fall':
        return round(random.uniform(5, 25), 1)
    else:
        return "Invalid season"

def main():
    
    month = int(input("Please enter the month number (1-12): "))

    if 3 <= month <= 5:
        season = 'spring'
    elif 6 <= month <= 8:
        season = 'summer'
    elif 9 <= month <= 11:
        season = 'autumn'
    else:
        season = 'winter'

    temperature = get_random_temp(season)

    print(f"The temperature right now is {temperature} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif 0 <= temperature <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif 16 < temperature <= 23:
        print("A pleasant temperature! Perfect for a walk outside.")
    elif 24 <= temperature <= 32:
        print("Getting warm! Make sure to stay hydrated.")
    else:  
        print("It's really hot out there! Stay cool and wear sunscreen.")

main()

#Ex8: 

