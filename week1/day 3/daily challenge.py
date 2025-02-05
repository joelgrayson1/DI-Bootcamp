Ex1:

user_word = input('enter your word')
print(type(user_word))
user_dict = {}
for key, value not in user_dict:
    if value not in user_dict:
    user_dict[value]=[]
else:
user_dict[value].append(key)
print(user_dict)

Ex 2:

def affordable_items(dictionary_wallet):
    affordable = []
    wallet = money_converter(wallet)
    for key, value in dictionary.items():
        value = money_converter(value)
        if value < wallet:
            affordable.append(key)
    if affordable != []:
        return sorted(affordable)
    else:
        print('Nothing')

print('\nExamples\n')

def money_convert(money):
    return int(money[1: ].replace(',', ' '))

def affordable_items(dictionary, wallet):
    affordable = []
    wallet = money_convert(wallet)
    for key, value in dictionary.items():
        value = money_converter(value)
        if value < wallet:
            affordable:append(key)
        if affordable != []:
            return sorted(affordable)
        else:
            return print('Nothing')

print('\nExamples\n')

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = '$300'

print(affordable_items(items_purchase, wallet))

items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = '$100'

print(affordable_items(items_purchase, wallet))

items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$1" 

print(nothing)

