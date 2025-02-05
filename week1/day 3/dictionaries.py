# Dictionaries: Data structure (more complex) because it holds key: value pairs
#ordered and mutable 

user_info = {'name':'Ron',
             'last_name: Weasley'
             'age': 17,
             'address': 'Ottery Village - England',
             'family': [('Arthur', 'Father', 50), ('Molly', 'Mother', 48)],
             'hobbies': {'Quaddrich', 'Swimming'}
}


#accesing values
print(user_info['name'])
print(user_info['family'][0])

sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict['class']['student']['marks']['history'])

#print(sample_dict[0]) #KeyError

ids_dict = {0: 123, 
            1:456,
            2: 678}

print(ids_dict[1])

#modify an entry
user_info['age'] = 18
print(user_info)

#Adding a new entry
user_info['School'] = 'Hogwarts'
print(user_info)

#Deleting an entry
del user_info['School']

print(user_info)

print('hobbies' in user_info)
print('birthdate' in user_info)

if 'birthday' in user_info:
    print(user_info['birthday'])
else:
    print('this key does\'t exists')

for relative in user_info['family']:
    print(relative)

student_info = {
    'name':'John',
    'age':25,
    'hobbies':['reading', 'gaming', 'cycling'],
    'city': 'New York'
}

student_info['age'] = 30
print(student_info)

student_info['Occupation'] = 'Engineer'
print(student_info)

del student_info['city']

if 'email' not in student_info:
    student_info['email'] = 'name@gmail.com'

print(student_info)

for hobbie in student_info['hobbies']:
    print(student_info)

#Built in methods
#print(user_info.keys())
#print(user.info.values())

for value in user_info.values():
    print(value)

sample_dict = {
    'name': 'Kelly',
    'age':25,
    'salary': 8000,
    'city': 'New York'
}

keys_to_remove = ['name', 'salary']

for key_remove in keys_to_remove:
    if key_remove in sample_dict.keys():
        del sample_dict[key_remove]
print(sample_dict)

car = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}

car.update({'model': 'Mazda'})
print(car)

#ZIP = Very useful built-in method

names = ['Lea', 'Darth Vaider', 'Luke', 'Chuwbacca']
power = [150, 500, 489, 100]

star_wars = dict(zip(names,power))
print(star_wars)

for char_name in names:
    if char_name == 'Darth Vaider':
        continue
    print(char_name)
    

               