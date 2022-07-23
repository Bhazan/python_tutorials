
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

object_1 = Person("sachin", 23)
print(object_1.name)
print(object_1.age)

class A:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def fullName(self):
        print("My Name is "+self.fname+" "+self.lname)
    

object_2 = A("Bhajan", "Singh")
object_2.fullName()
