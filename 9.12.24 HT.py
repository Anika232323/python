'''QUESTION 1:
class Camera:
    def __init__(self,resolution):
        self.resolution=resolution
    def takephoto(self):
        print(f"The photo is taken in {self.resolution} resolution")
class Phone:
    def __init__(self,phonenumber):
        self.phonenumber=phonenumber
    def makecalls(self,number):
        print(f"Calling {number} from {self.phonenumber}")
    def sendmsg(self,number,message):
        print(f"Sending to {number} from {self.phonenumber}: {message}")
class Smartphone(Camera,Phone):
    def __init__(self,resolution,phonenumber,brand,model):
        Camera.__init__(self,resolution)
        Phone.__init__(self,phonenumber)
        self.brand=brand
        self.model=model
    def display(self):
        print("Brand of the Smartphone:",self.brand)
        print("Model of the Smartphone:",self.model)
        print("Camera resolution of the Smartphone:",self.resolution)
        print("Phonenumber:",self.phonenumber)
details=Smartphone("1600 pixels",8939219826,"Vivo Y20","V2029")
details.display()
details.takephoto()
details.makecalls(9361381411)
details.sendmsg(9361381411,"Iam missing you so badly")'''

class Student:
    def studentInfo(self,name,course):
        self.name=name
        self.course=course
    def displayInfo(self):
        print("Name of the student:",self.name)
        print("Course:",self.course)
class StudentAthlete(Student):
    def __init__(self,name,course,sport):
        Student.studentInfo(self,name,course)
        self.sport=sport
    def displayAtheleteInfo(self):
        self.displayInfo()
        print("Sport:",self.sport)
s=StudentAthlete("Anika","AI","Badminton")
s.displayAtheleteInfo()
