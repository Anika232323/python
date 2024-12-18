#getter and setter method
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self): #getter method
        return self.name
    def get_age(self):
        return self.age
    def set_name(self,name):#setter method
        self.name=name
    def set_age(self,age):
        self.age=age
name=input("Enter name:")
age=int(input("Enter age:"))
#1 method
s=Student(name,age)
#2nd method this also can be used... Don't use both at the same time.
n=input()
s.set_name(n) #name will get modified
print(f"Name: {s.get_name()}\nAge: {s.get_age()}")
