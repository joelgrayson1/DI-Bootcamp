#Tuples: immmutable and ordered

numbers = (10, 20, 30, 40, 20, 50, 20)
print(type(numbers))

# numbers[1] = 25 # error: not possible to change an element

print(numbers[1])

#methods

print(numbers.count(20))
print(numbers.index(30))

#Concatenate tuples
numbers2 = (2,3,5,7)
mixed_tuples = numbers + numbers2
print(mixed_tuples)

students = ['Joel']
print(students)

my_tuple = (1,2)
print(type(my_tuple))

#unpacking a tuple
a,b,c,d = (5,10,15,20)
print(a)
print(b)
print(c)
print(d)

a,b,c,d = (10,20,30,40)
print(a)
print(b)
print(c)
print(d)

#Sets = unordered data structure

my_set = {1,4,8,9}
# my_set = set()

my_set.add(12)
my_set.add(55)
print(my_set)

fav_numbers = {22,26,28,29}
fav_numbers.add(30)
print(fav_numbers)

prime_numbers = {3, 5, 7, 11}
print(fav_numbers.intersection(prime_numbers))
fav_numbers.clear



