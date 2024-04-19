class Box:
    def _init_(self,name,roll):
        self.name=name
        self.roll=roll

class Box2(Box):
    def _init_(self,name,roll,marks):
        self.marks=marks
        Box._init_(self,name,roll)

b1=Box2("riya",52,92)
print(b1.name)
print(b1.roll)
print(b1.marks)
