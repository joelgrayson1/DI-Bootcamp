#Ex1

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

bengal_cat = Bengal(name="Leo", age=3)
chartreux_cat = Chartreux(name="Milo", age=4)
siamese_cat = Siamese(name="Luna", age=2)

all_cats = [bengal_cat, chartreux_cat, siamese_cat]

sara_pets = Pets(all_cats)

sara_pets.walk()

#Ex2:

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_dog_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_dog_power:
            return f"{self.name} wins the fight"
        elif self_power < other_dog_power:
            return f"{other_dog.name} wins the fight"
        else:
            return "Draw!"

dog1 = Dog(name="Louie", age=2, weight=22)
dog2 = Dog(name="Tommy", age=6, weight=20)
dog3 = Dog(name="Sam", age=8, weight=17)

print(dog1.bark())  
print(dog2.bark())  
print(dog3.bark())  

print(dog1.fight(dog2))  
print(dog2.fight(dog3))  
print(dog1.fight(dog3)) 

#Ex3



#Ex 4

class Family:
    def __init__(self, last_name, members=[]):
        self.last_name = last_name
        self.members = []
        for member in member:
            self.members.append({'name': member})

    def born(self, **kwargs):
        print('Congratulations on a new member of the family')
        self.members.append(kwargs)
    
    def is_18(self, member_name):
        person_to_find = None
        for member in self.members:
            if member.name == member_name:
                if member.age >= 18:
                    return True
                else:
                    return False
    
    def family_presentation(self):
        print(f'{self.last_name} family details')
        for member in self.members:
            for details in member.keys():
                print(f'{detail}: {member[detail]}')

my_family = Family('Wolf')
my_family.born(name='Aaron', age='411')
my_fam = Family('Wolf', me)

my_family.family_presentation()

#Ex5

