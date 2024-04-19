class Box:
    def _init_(self,name,roll):
        self.name=name
        self.roll=roll

class Student:
    def _init_(self,fees):
        self.fees=fees

class Box2(Box,Student):
    def _init_(self,name,roll,marks,fees):
        self.marks=marks
        Box._init_(self,name,roll)
        Student._init_(self,fees)



b1=Box2("riya",52,92,58000)
print(b1.name)
print(b1.roll)
print(b1.marks)
print(b1.fees)
