
class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printName(self):
        print("My Name is "+self.fname+" "+self.lname) 

obj = Person("Bhajan", "Singh")
obj.printName()