#Ex1:

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))
print(result)

#Ex2:

def ticket_price(age):
    if age < 3:
        return 0
    elif 3 <= age <= 12:
        return 10
    else:
        return 15


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

for name, age in family.items():
    total_cost += ticket_price(age)

print(f"Total cost for the family: ${total_cost}")


def ticket_price(age):
    if age < 3:
        return 0
    elif 3 <= age <= 12:
        return 10
    else:
        return 15

family = {}

while True:
    name = input("Enter family member's name (or type 'done' to finish): ")
    if name.lower() == 'done':
        break
    age = int(input(f"Enter {name}'s age: "))
    family[name] = age


total_cost = 0

for name, age in family.items():
    total_cost += ticket_price(age)

print(f"Total cost for the family: ${total_cost}")

#Ex3:

brand = {
    "name": "Zara",
    "creation_date": 1975, 
    "number_stores": 2, 
    "type_of_clothes": ["casual", "formal", "sportswear"],
    "major_color": {"US": "Blue", "Spain": "Red", "UK": "Green"},
    "international_competitors": ["H&M", "Uniqlo"]
}

print(f"Zara's clients are looking for {', '.join(brand['type_of_clothes'])}")

brand['country_creation'] = 'Spain'

if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

del brand["creation_date"]

print(f"The last international competitor is {brand['international_competitors'][-1]}.")

print(f"The major clothes color in the US is {brand['major_color']['US']}")

print(f'The dictionary contains {len(brand)} key-value pairs.')

print('The keys of the dictionary are:', brand.keys())

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

brand.update(more_on_zara)

print(f"The updated number of stores is {brand['number_stores']}.")


#Ex4

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]


disney_users_A = {}
for index, user in enumerate(users):
    if 'i' in user or user[0].lower() in ['m', 'p']:
        disney_users_A[user] = index

print(disney_users_A)

disney_users_B = {}
for index, user in enumerate(users):
    disney_users_B[index] = user

print(disney_users_B)

disney_users_C = {user: index for index, user in enumerate(sorted(users))}

print(disney_users_C)
