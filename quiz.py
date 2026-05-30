class Menu:
    dish_of_the_day = "spam"

print(Menu.dish_of_the_day)

class Dog:
    def __init__(name, age):
        self.name = name
        self.age = age

dog = Dog("Pinky", 3)
print(dog.name)