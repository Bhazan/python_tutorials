 
class B:
    def __init__(para_self, para1, para2):
        para_self.fname = para1
        para_self.lname = para2

    def fullName(para_self):
        print("My Name is "+para_self.fname+" "+para_self.lname)

obj1 = B("Bhajan", "Singh")
obj1.fullName()

class C:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = C("Bhajan", 25)
print(obj.name)
print(obj.age)
# Update properties of obj object of class C below
obj.name = "Mahendra"
obj.age = 42
print(obj.name)
print(obj.age)
# delete object
del obj
# print(obj.name) this throw error
