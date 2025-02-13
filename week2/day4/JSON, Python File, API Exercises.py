#ex1

def get_words_from_file(sowpods.txt):
    try:
        with open(sowpods.txt, 'r') as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        print("The file was not found. Please ensure the file is in the correct location.")
        exit()

def get_random_sentence(length, word_list):
    if length < 2 or length > 20:
        print("Error: Sentence length must be between 2 and 20.")
        exit()
    
    random_words = random.sample(word_list, length)
    
    sentence = ' '.join(random_words).lower()
    return sentence

def main():
    print("Welcome to the random sentence generator!")
    print("This program generates a random sentence from a word list.")
    
    try:
        length = int(input("How long do you want the sentence to be? (between 2 and 20): "))
        
        if length < 2 or length > 20:
            print("Error: Please enter a number between 2 and 20.")
            return
        
        words = get_words_from_file('sowpods.txt')
   
        sentence = get_random_sentence(length, words)
        print("Generated sentence:", sentence)
        
    except ValueError:
        print("Invalid input. Please enter an integer between 2 and 20.")
        return

if __name__ == "__main__":
    main()

#Ex2

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

salary = data["company"]["employee"]["payable"]["salary"]
print(f"Salary: {salary}")

data["company"]["employee"]["birth_date"] = "1994-01-22"

with open("updated_employee.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("The updated JSON has been saved to 'updated_employee.json'.")
