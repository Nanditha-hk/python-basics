class Box:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

class Student:
    def __init__(self,fees):
        self.fees=fees

class Box2(Box,Student):
    def __init__(self,name,roll,marks,fees):
        self.marks=marks
        Box._init_(self,name,roll)
        Student._init_(self,fees)

class Box3(Box2):
    def __init__(self,sem):
        self.sem=sem
        Box2._init_(self,"ABCD",25,80,52000)

b1=Box2("riya",52,92,58000)
print(b1.name)
print(b1.roll)
print(b1.marks)
print(b1.fees)


b2=Box3("3rd sem")
print(b2.sem)
