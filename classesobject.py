#A class is a blueprint of an object
#object is an instance of a class

class Person:
    #Properties /Attributes/Variables/Characteristics
    name="James"
    age=23
    gender="Female"

    #Methods/Functions/Behaviours
    def move(self):
        print("Person is walking")

farmer=Person()
farmer.move()
print(farmer.gender)

doctor=Person()
doctor.move()