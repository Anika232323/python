'''#public
class Student:
    id=int(input())#public
    def __init__(self):
        self.__name=input("Enter the name:")#private
        self.__age=input("Enter age:")#private
    def display(self):
        print("Name=",self.__name)
        print("Age=",self.__age)
s= Student()
s.display()
print(s.id)
#private gives error
class Student:
    __id=234#private("__" this symbol is for private)
    def __init__(self,name):
        self.__name=name
    def display(self):
        print("Name=",self.__name)
s= Student("Anika")
s.display()
print(s.id)
#
class Student:
    id=int(input("Enter ID:"))#public
    def __init__(self):
        self.name=input("Enter the name:")#public
        self.__age=input("Enter age:")#private
        self.__course=input("Enter Course:")#private
s= Student()
print("Name:",s.name)
print("Age:",s._Student__age)
print("Course:",s._Student__course)'''

class person:
    id=int(input("Enter ID:"))
    def __init__(self):
        self.__name=input("Enter name:")
        self.__age=int(input("Enter age:"))
class student(person):
    def __init__(self):
        self.stu_id=input("Enter student id:")
class Employee(person):
    def __init__(self):
        self.__emp_id=input("Enter Employee id:")

class Display_details(student,Employee,person):
    def __init__(self):
        person.__init__(self)
        student.__init__(self)
        Employee.__init__(self)

m=Display_details()
print(f"Name of the person: {m._person__name}\nAge of the person: {m._person__age}")
print(f"Student Id: {m.stu_id}")
print(f"Employee Id: {m._Employee__emp_id}")
