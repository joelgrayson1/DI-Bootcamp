#Ex1:

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s" if self.amount != 1 else f"{self.amount} {self.currency}"

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return Currency(self.currency, self.amount + other.amount)
        elif isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Currency' and '{type(other).__name__}'")

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        elif isinstance(other, int):
            self.amount += other
        else:
            raise TypeError("Unsupported operand type(s) for +=: 'Currency' and '{type(other).__name__}'")
        return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))  
print(int(c1))  
print(repr(c1))  

c1_plus_5 = c1 + 5
print(c1_plus_5)  

c1_plus_c2 = c1 + c2
print(c1_plus_c2) 

print(c1)  

c1 += 5
print(c1)  

c1 += c2
print(c1)  

try:
    c1 + c3
except TypeError as e:
    print(e)

#E2 - In func and exercise_one files

#Ex3 

import random
import string

def generate_random_string(length=5):
    characters = string.ascii_letters 
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

random_str = generate_random_string(5)
print(random_str)

#Ex4

import datetime

def display_current_date():
    current_date = datetime.date.today()
    print(f"Today's date is: {current_date}")

display_current_date()

#Ex5

import datetime

def time_until_new_year():
    now = datetime.datetime.now()
    
    next_year = now.year + 1  
    new_year = datetime.datetime(next_year, 1, 1)
    
    time_left = new_year - now
    
    days_left = time_left.days
    hours_left = time_left.seconds // 3600
    minutes_left = (time_left.seconds % 3600) // 60
    seconds_left = time_left.seconds % 60
    
    print(f"The 1st of January is in {days_left} days, {hours_left} hours, {minutes_left} minutes, and {seconds_left} seconds")
    
time_until_new_year()

#Ex6

import datetime

def calculate_minutes_lived(birthdate):
    birth_date = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
    
    current_date = datetime.datetime.now()
    
    time_lived = current_date - birth_date
    
    minutes_lived = time_lived.total_seconds() / 60
    
    print(f"You have lived for approximately {int(minutes_lived)} minutes.")

birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
calculate_minutes_lived(birthdate_input)

#Ex7


