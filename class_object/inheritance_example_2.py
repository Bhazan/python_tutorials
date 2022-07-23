# Parent class  is given below
class A:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def printName(self):
        print("My Name is "+self.fname+" "+self.lname)

objA = A("Bhajan","Singh")
objA.printName()

# Child class is given below that inherits all property of parent class A

class B(A):
    def __init__(self, fname, lname, age):
        A.__init__(self, fname, lname) # We can also use super().__init__(self, fname, fname)
        self.age = age

    def printInfo(self):
        print(self.fname + " "+ self.lname, self.age)


child_object = B("Bhajan", "Singh", 26)
child_object.printInfo()
