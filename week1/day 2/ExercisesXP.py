#Exercise 1
my_fav_numbers = {22,26,28,29}

my_fav_numbers.add(10)
my_fav_numbers.add(20)
print(my_fav_numbers)

my_fav_numbers.remove(29)
print(my_fav_numbers)

friend_fav_numbers = {13,19,23,24}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#Exercise 2
#No because tuples are immutable so the elements can't be added.

#Exercise 3
basket = ['banana', 'apples', 'oranges', 'blueberries']
basket.remove('banana')
print(basket)
basket.remove('blueberries')
print(basket)
basket.append('kiwi')
print(basket)
basket.insert(0, 'apples')
print(basket)
apple_count = basket.count('apples')
print(f'number of apples in the basket: {apple_count}')
basket.clear()
print(basket)

#Exercise 4
#A float ia a decimal number or whole number. An integer is a whole number and not a decimal.

#Exercise 5
for num in range(1,21):
    print(num)
for i in range(1,21):
    if i % 2 == 1:
        print(i)

#Exercise 6
my_name = 'Joel'

while True:
    user_name = input('What is your name?')

    if user_name == my_name:
        print('Hey Joel')
        break
    else:
        print('Not my name')

#Exercise 8

#Exercise 9 
total_cost = 0
num_people = int(input('How many people are in the family?'))
for i in range(num_people):
    age = int(input(f'Enter the age of person {i + 1}:'))
    if age < 3:
        print('Ticket is free')
        ticket_price = 0
    elif 3 <= age <= 12:
        print('Ticket costs $10')
        ticket_price = 10
    else:
        print('Ticket costs £15')
        ticket_price = 15

total_cost += ticket_price
print(f'\nThe totalcost for the family ticket is: ${total_cost}')

#Exercise 10
sandwich_orders = ['tuna sandwich', 'pastrami sandwich', 'avocado sandwich', 'pastrami sandwich', 'egg sandwich', 'chicken sandwich', 'pastrami sandwich']
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print(f'I made your {sandwich.lower()}')
    