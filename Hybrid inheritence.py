class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def person_info(self):
        print(f"Name of the person: {self.name}\nAge of the person: {self.age}")
class student(person):
    def __init__(self,stu_id):
        self.stu_id=stu_id
    def student_info(self):
        print(f"Student Id: {self.stu_id}")
class Employee(person):
    def __init__(self,emp_id):
        self.emp_id=emp_id
    def Employee_info(self):
        print(f"Employee Id: {self.emp_id}")
class Display_details(student,Employee,person):
    def __init__(self,name,age,stu_id,emp_id):
        person.__init__(self,name,age)
        student.__init__(self,stu_id)
        Employee.__init__(self,emp_id)
    def display_all(self):
        self.person_info()
        self.student_info()
        self.Employee_info()
m=Display_details("Anika",18,"E24AI003",207645)
m.display_all()


