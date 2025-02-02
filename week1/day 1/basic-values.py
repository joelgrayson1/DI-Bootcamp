# BASIC VALUE TYPES

print('Hello world')

print (8 +2 )

print(5.75 + 3.10)
print (type(5.35))

5
2.54
'Good Morning'
print(type(5))
print(type(False))

print (5 > 7)

# Value Types: Integers, Floats, Strings and Booleans

#string = sequence of chars. So I can use indexing
name = 'Joel'
print(name[3])

#len () = discover the length of the string
print (len('Harry Potter'))
#exercise: create a variable called my_name . assign it to your name as a string
# print the middle letter of your name 
# print just the second letter as your name
# print just the 3 or 2 last letters of your name 

name = 'Joel Grayson'

print (name.capitalize())
print (name.title())
print (name.lower_())

name.replace('Grayson', 'Granger')

user_name = ' Joel Grayson'
cleaned_user_name = user_name.script('!')
print(cleaned_user_name)

price = '$100'
cleaned_price = price.strip('$')
print(cleaned_price)

#Type Casting (changing the type of a value)
user_age_int = float(my_height)

print(user_age_int)
print(float(1))

print('hello world' * 4)

print(Joel) 

first_name= 'Joel'
last_name = 'Grayson'
full_name = first_name + ' ' + last_name
print(full_name)
