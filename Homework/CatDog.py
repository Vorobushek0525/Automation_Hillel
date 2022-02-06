class Cat:
    weight = 5
    length = 40

cat_Tom = Cat()

# print(cat_Tom.weight)

class Dog:
    weight = 40
    length = 100

dog_Jack = Dog()

class CatDog:

    CatDog.weight = (cat_Tom.weight + dog_Jack.weight)
    CatDog.length = (cat_Tom.length + dog_Jack.length)

CatDog = CatDog()

print(CatDog.weight)

