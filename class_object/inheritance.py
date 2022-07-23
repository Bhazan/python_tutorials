# an inheritance example Person is parent class 
class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printName(self):
        print("My Name is "+self.fname+" "+self.lname) 

obj = Person("Bhajan", "Singh")
obj.printName()

# below is a child class named Student

class Student(Person):
    pass # if you don't want any property here all property inherit from parent class

student1 = Student("Virat", "Kohli")
student1.printName()