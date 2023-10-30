# class Dog():

#     # Class object attribute
#     species = "mammal"

#     # __(name)__ is the naming for special methods
#     # init is short for initialization
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name

# mydog = Dog(breed = "Lab", name = "Sammy")
# print(mydog.breed)
# print(mydog.name)


class Circle():
    pi = 3.14
    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi
    
    def set_radius(self, new_r):
        self.radius = new_r
    
myc = Circle(3)
myc.set_radius(999)
print(myc.area())


# INHERITANCE

class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("DOG CREATED")

    def bark(self):
        print("WOOF")

    def eat(self):
        print("DOG EATING")


myd = Dog()
myd.whoAmI()
myd.eat()
myd.bark()
