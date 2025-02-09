#Ex1:

input_string = input("Enter a comma-separated sequence of words: ")

sorted_words = ','.join(sorted([word for word in input_string.split(',')]))

print("Sorted words:", sorted_words)

#Ex2

def longest_word(sentence):
    
    words = sentence.split()
    
    longest = words[0]
    
    for word in words:
        if len(word) > len(longest):
            longest = word
    
    return longest

print(longest_word("I found fifteen flowers today."))  
print(longest_word("When I saw her at the beach I ran over right away.")) 
print(longest_word("Football is the most popular sport in England"))  
