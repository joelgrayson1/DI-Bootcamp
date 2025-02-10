#Ex1

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Snowy", 2)
cat2 = Cat("Stormy", 5)
cat3 = Cat("Marty", 8)

def find_oldest_cat(cats):
    oldest_cat = cats[0]
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

cats = [cat1, cat2, cat3]

oldest = find_oldest_cat(cats)

print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")

#Ex2

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

print(f"David's dog: {davids_dog.name}, Height: {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

print(f"Sarah's dog: {sarahs_dog.name}, Height: {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}.")
else:
    print(f"The bigger dog is {sarahs_dog.name}.")

#Ex3

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song([
    "There's a lady who's sure",
    "all that glitters is gold",
    "and she's buying a stairway to heaven"])

stairway.sing_me_a_song()

#Ex4

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} added to {self.name}.")
        else:
            print(f"{new_animal} is already in the zoo.")

    def get_animals(self):
        if self.animals:
            print(f"Animals in {self.name}:")
            for animal in self.animals:
                print(animal)
        else:
            print(f"No animals in {self.name}.")
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} sold from {self.name}.")
        else:
            print(f"{animal_sold} not found in the zoo.")

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        animal_groups = {}

        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in animal_groups:
                animal_groups[first_letter] = [animal]
            else:
                animal_groups[first_letter].append(animal)

        return animal_groups

    def get_groups(self):
        animal_groups = self.sort_animals()
        print(f"Animal groups in {self.name}:")
        for letter, animals in animal_groups.items():
            print(f"{letter}: {', '.join(animals)}")

ramat_gan_safari = Zoo("Ramat Gan Safari")

ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Emu")

ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Cat")

ramat_gan_safari.get_animals()

ramat_gan_safari.get_groups()
