#Exercise 1: Pets

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

bengal = Bengal("Leo", 2)
chartreux = Chartreux("Max", 3)
siamese = Siamese("Luna", 4)

all_cats = [bengal, chartreux, siamese]

sara_pets = Pets(all_cats)

sara_pets.walk()


#Exercise 2: Dogs

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} won the fight"
        else:
            return f"{other_dog.name} won the fight"

dog1 = Dog("Buddy", 4, 20)
dog2 = Dog("Charlie", 3, 25)
dog3 = Dog("Max", 5, 30)

print(dog1.bark())
print(dog1.run_speed())
print(dog1.fight(dog2))


#Exercise 3: Dogs Domesticated

import random

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        self.trained = True
        print(self.bark())
        print(f"{self.name} is now trained")

    def play(self, *args):
        dog_names = [dog.name for dog in args]
        print(f"{', '.join(dog_names)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet!")

pet_dog = PetDog("Rex", 3, 15)
pet_dog.train()
pet_dog.do_a_trick()
pet_dog.play(dog1, dog2)


#Exercise 4: Family


class Family():
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations! {kwargs['name']} is born!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Family Last Name: {self.last_name}")
        for member in self.members:
            print(f"{member['name']} ({member['age']} years old, {member['gender']}, {'Child' if member['is_child'] else 'Adult'})")

family = Family(
    last_name="Smith",
    members=[
        {'name':'Michael', 'age':35, 'gender':'Male', 'is_child': False},
        {'name':'Sarah', 'age':32, 'gender':'Female', 'is_child': False}
    ]
)

family.family_presentation()
family.born(name="Baby Jack", age=0, gender="Male", is_child=True)
family.family_presentation()
print(family.is_18("Michael"))



#Exercise 5: The Incredibles Family


class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['name']} uses their power: {member['power']}")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old.")
    
    def incredible_presentation(self):
        print("Here is our powerful family:")
        super().family_presentation()

incredibles = TheIncredibles(
    last_name="Incredibles",
    members=[
        {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
        {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
    ]
)

incredibles.incredible_presentation()

incredibles.born(name="Baby Jack", age=0, gender="Male", is_child=True, power="Unknown Power", incredible_name="BabyJack")

incredibles.incredible_presentation()

incredibles.use_power("Michael")