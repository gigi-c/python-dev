class Animal():
    animal_kind = "Canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return ("{} says I am eating Chicken".format(self.name))
