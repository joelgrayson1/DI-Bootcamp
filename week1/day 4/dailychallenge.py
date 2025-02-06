MATRIX_STRING = '''7i3
Tsi
h%x
i #
sM 
$a 
#t%
^r!'''

# [['7i3'], ['Tsi'], [h%x], ['7i3']]

#Steps:
# 1 - to create a 2D List
# 2 - decrypt the matrix: for loop, check characters
# 3 - replace every group of symblos between two alpha characters with a space
# 4 - output a string with the message

#step 1: create like [['7i3'], ['Tsi'], [h%x], ['7i3']]

matrix = []

for i in range(len(MATRIX_STRING)):
    row = list(MATRIX_STRING[i:i+3])
    MATRIX_STRING.split
    print(row)
    matrix.append(row)
print(matrix)

row = MATRIX_STRING.split('\n')
print(row)

for row in rows:
    matrix.append(list(row))

print(matrix)

for column in matrix:
    column_0 = [column[0] for column in matrix] #creates list inside matrix
    column_1 = [column[1] for column in matrix]
    column_2 = [column[2] for column in matrix]

column_matrix = []
column_matrix.append(column_0)
column_matrix.append(column_1)
column_matrix.append(column_2)

print(column_matrix)

output_string = ''
for sublist in matrix:
    #print(sublist)
    for i in range(len(sublist)):
        if sublist[i].isalpha():
            output_string += sublist[i]
        else:
            if len(output_string) != 0 and output_string [-1] != ' ':
                output_string += ' '
print(output_string)

