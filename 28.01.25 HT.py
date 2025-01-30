#1
from abc import ABC,abstractmethod
class Abstract_method(ABC):
    @abstractmethod
    def welcome(self):
        pass
    def TestData(self):
        pass
    def vowel_count(self):
        pass
    def grade(self):
        pass

class Student_details(Abstract_method):
    def __init__(self,name,mark1,mark2):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
    def welcome(self):
        print("Welcome To WTS! We wish you the Best!!")
    def TestData(self):
        print(f"Welcome {self.name}!\nHave a nice day!")
    def vowel_count(self):
        vow={}
        for i in self.name:
            if i in "AEIOUaeiou"and i not in vow:
                vow[i]=1
        count=sum(vow.values())
        print(f"Count of Vowels are : {count}")
        for i,j in vow.items():
            print(f"{i}:{j}")
    def grade(self):
        tot=self.mark1+mark2
        per=(tot/200)*100
        if per>95:
            print("Grade E")
        elif per>75 and tot<=80:
            print("Grade A+")
        elif per>=60 and tot<=75:
            print("Grade A")
        elif per>=50 and tot<=60:
            print("Grade B")
        else:
            print("Grade F")
name=input("Please input a name :")
mark1=int(input("Please enter mark1:"))
mark2=int(input("Please enter mark2:"))
s=Student_details(name,mark1,mark2)
s.welcome()
s.TestData()
s.vowel_count()
s.grade()

#2
#b1
user=input("Enter your input-")
for i in range(len(user)):
    if user[i].isdigit():
        print(user[0:i])
        break

#b2
user=input("Enter your input-")
for i in range(len(user)):
    if user[i].isdigit():
        continue
    else:
        print(user[i],end="")
