number = int(input('enter a number:'))
length = int(input('enter length of the list:'))
multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)
print(multiples)


user_word = input('enter word: ')
new_word = ''
for i in range(len(user_word)):
    if i == 0 or user_word[i] != user_word[i-1]:
        new_word += user_word[i]
print(f'new word: {new_word}')
