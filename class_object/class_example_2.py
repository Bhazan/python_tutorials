 
class B:
    def __init__(para_self, para1, para2):
        para_self.fname = para1
        para_self.lname = para2

    def fullName(para_self):
        print("My Name is "+para_self.fname+" "+para_self.lname)

obj1 = B("Bhajan", "Singh")
obj1.fullName()