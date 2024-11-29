class Employee:
    def __init__(self,emp_id,emp_name,emp_position):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_position=emp_position
    def displayEmployeeInfo(self):
        print(f"Name:{self.emp_name}\nId:{self.emp_id}\nPosition:{self.emp_position}")
class Address:
    def __init__(self,street,state,country):
        self.street=street
        self.state=state
        self.country=country
    def displayAddress(self):
        print(f"Street Name:{self.street}\nState Name:{self.state}\nCountry Name:{self.country}")
class EmployeeDetails(Employee,Address):
    def __init__(self,emp_id,emp_name,emp_position,street,state,country):
        super().__init__(emp_id,emp_name,emp_position)
        Address.__init__(self,street,state,country)
    def displayEmp(self):
        self.displayEmployeeInfo()
        self.displayAddress()

ed=EmployeeDetails("Jiya",100,"Manager","Shenoy Nagar","TamilNadu","India")
ed.displayEmp()









        
        
        
