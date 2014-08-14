# -*- coding:utf-8 -*-

class Animal(object) :
    
    def show(self) :
        print "I'm a Animal"


#Dog is a Animal
class Dog(Animal):

#constructor function
    def __init__(self, name):
        #Dog has a name
        self.name = name

            
#Cat is a Animal
class Cat(Animal):

    def __init__(self, name):
        #Cat has a name
        self.name = name

#abstract class
class Person(object):        

    def __init__(self, name):
        #Person has a name
        self.name = name
        #Person has a pet of some function
        self.pet = None

    def show(self):
        print "I'm a Person"
        
class Employ(Person):

    def __init__(self, name, salary):
        super(Employ, self).__init__(name)
        #Employ has a salary
        self.salary = salary

#Abstract class
class Fish(object):        
    
    def show(self) :
        print "I'm a Fish"
#Halibut is a Fish
class Halibut(Fish):
    pass
#Salmon is a Fish
class Salmon(Fish):
    pass

#rover is a Dog ,init its name of Dog
rover = Dog("Rover")
rover.show()

#satan is a Cat, init its name of Cat
satan = Cat("Satan")


#mary is a Person , her name is mary
mary = Person("Mary")
mary.show()

mary.pet = satan

#init the class of Employ
frank = Employ("Frank", 120000)

frank.pet = rover

#flipper is a Fish
flipper = Fish()

crouse = Salmon()

harry = Halibut()




