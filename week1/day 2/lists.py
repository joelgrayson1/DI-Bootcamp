my_name = 'Jack'
hello = 'Hello World'
my_age = 27

my_list = [my_name, hello, my_age]

#Lists syntax
numbers = [1,2,3,47,9]
print(numbers)

#ordered darta structure sequence = we can use index
print(numbers[3])

#mutable = I can change it
numbers[3] = 55
print(numbers)

#list methods
students = ['Harry', 'Ron', 'Hermione']
students.append('Luna')

print(students)

students.insert(1, 'Ginny')
print(students)

students.remove('Ron')
print(students)

students.append( 'Ginny')
print(students)

students.pop(1)
print(students)

#Exercise
#Given this list:
#list1 = [5,10,15,20,25,50,20]
# print index 3
#change 50 to 70
# delete number 20
# add a new number to the end of the list

numbers = [5,10,15,20,25,50,20]
print(numbers)

print(numbers[3])

numbers[5] = 70
print(numbers)

numbers.remove(20)
print(numbers)

numbers.append(77)
print(numbers)

#method to check after the class
# copy()
# extend()
# clear()
# sort()

#Tuples are immutable lists, items can;t be changed.