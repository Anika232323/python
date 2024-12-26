#1
def check(user):
    if len(user)>=10:
        if user[0]=='(' and user[4]==')' and user[9]=='-':
            return "Valid"
        elif user[3]=='-' and user[7]=='-':
            return "Valid"
        elif user.isdigit():
            return "Valid"
        else:
            return "Invalid"
    else:
        return " Invalid phone number"
user=input("Enter phone number:")
print(check(user))

#2
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def set_name(self,name):
        if len(self.name)!=0:
            if self.name.isalpha():
                return "Valid"
            else:
                raise ValueError("Non-string")
        else:
                raise ValueError("Empty string")
        
    def get_name(self):
        if self.set_name(name)=="Valid":
            return self.name
        else:
            self.set_name(name)

    def set_marks(self,marks):
        if 0<self.marks<=100:
            return "Valid"
        else:
            raise ValueError("Out of range")

    def get_marks(self):
        if self.set_marks(marks)=="Valid":
            return self.marks
        else:
            self.set_marks(marks)

    def calculate_grade(self,marks):
        if 90<=self.marks<=100:
            return "Grade A"
        elif 80<=self.marks<=89:
            return "Grade B"
        elif 70<=self.marks<=79:
            return "Grade C"
        elif 60<=self.marks<=69:
            return "Grade D"
        else:
            return "Fail"
name=input("Enter  name:")
marks=int(input("Enter marks:"))
try:
    s=Student(name,marks)
    print("Student name:",s.get_name())
except ValueError as e:
    print(e)
try:
    s=Student(name,marks)
    print("Student marks:",s.get_marks())
    print("Grade:",s.calculate_grade(marks))
except ValueError as a:
    print(a)
    


