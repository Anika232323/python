#Input inside the function class
class College:
    def __init__(self):
        self.name=input("Enter your name:")
        self.course=input("Enter your course:")
    def studentDetails(self):
        print("Student name:",self.name)
        print("Course:",self.course)
class Talent:
    def __init__(self):
        self.hobbies=input("Enter your hobbies:")
    def display(self):
        print("Hobby:",self.hobbies)
class Event(College,Talent):
    def __init__(self):
        College.__init__(self)
        Talent.__init__(self)
        self.event_joined=input("Enter the event in which you want to participate in:")
    def EventInfo(self):
        self.studentDetails()
        self.display()
        print("Event joined:",self.event_joined)
v=Event()
v.EventInfo()

#Input outside the class
class College:
    def __init__(self,name,course):
        self.name=name
        self.course=course
    def studentDetails(self):
        print("Student name:",self.name)
        print("Course:",self.course)
class Talent:
    def __init__(self,hobbies):
        self.hobbies=hobbies
    def display(self):
        print("Hobby:",self.hobbies)
class Event(College,Talent):
    def __init__(self,name,course,hobbies,event_joined):
        College.__init__(self,name,course)
        Talent.__init__(self,hobbies)
        self.event_joined=event_joined
    def EventInfo(self):
        self.studentDetails()
        self.display()
        print("Event joined:",self.event_joined)
name=input("Enter your name:")
course=input("Enter your course:")
hobbies=input("Enter your hobbies:")
event_joined=input("Enter the event in which you want to join:")
v=Event(name,course,hobbies,event_joined)
v.EventInfo()
