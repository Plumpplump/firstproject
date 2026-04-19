class Person:

    amount = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1

    def helloWorld(self):
        print("helloWorld")

    def __del__(self):
        Person.amount -= 1

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}"
    
    def get_older(self):
        self.age += Person.amount