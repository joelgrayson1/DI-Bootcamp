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

