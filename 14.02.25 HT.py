class Employee_Management_System:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")
    def calculate_yearly_salary(self):
        yearly=12*self.salary
        print("Yearly salary:",yearly)

emp=Employee_Management_System("Anika","EMP003",50000)
emp.display_info()
emp.calculate_yearly_salary()
        
