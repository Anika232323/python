#QUESTION 1:
class User:
    def __init__(self):
        self.__username=input("Enter your username:")
        self.__password=input("Enter your password")
    def set_password(self):
        digit=False
        spl_char=False
        spl=[" ! ","@"," #", "$", "%", "^", "&", "*", " -" ,"_"]
        if len(self.__password)>=8:
            if any(i.isdigit() for i in self.__password):
                if any(i in spl for i in self.__password):
                    if self.__password[0].isupper()==True:
                        return "Valid"
                    else:
                        return "First character must be in capital"
                else:
                    return "Password should have at least one special character."
            else:
                return "Password should have at least one number."
        else:
            return "Password should be at least 8 characters long"
    def check_password(self):
        if self.set_password ()=="Valid":
            return "Password verified!!"
        else:
            return "Password verified--Invalid password"
u=User()
print(u.set_password())
print(u.check_password())

#QUESTION 2:
class Product:
    def __init__(self,name,price,stock):
        self.__name=name
        self.__price=price
        self.__stock=stock
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    
    def set_price(self,price):
        self.__price=price
        if self.__price>0:
            return "Price is valid"
        else:
            return "Price should not be less than 0"
    def set_stock(self,stock):
        self.__stock=stock
        if type(self.__stock)==int and self.__stock>0:
            return "Stock is valid"
        else:
            return " Stock should be an integer and non-negative."
    def get_stock(self):
        return self.__stock
name="iPhone"
price=80000
stock=100
p=Product(name,price,stock)
print(p.set_price(price))
print(p.set_stock(stock))
print("Stock is",p.get_stock())

#QUESTION 3:
class Student:
    def __init__(self,name,age,marks):
        self.__name=name
        self.__age=age
        self.__marks=marks
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if 5<self.__age>100:
            return "ValueError"
        else:
            return self.get_age()
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        if 0<self.__marks>100:
            return "ValueError"
        else:
            return self.get_marks()
    
name="Anika"
age=18
marks=98
s=Student(name,age,marks)
print("Name:",s.get_name())
print("Age:",s.set_age(age))
print("Marks:",s.set_marks(marks))
            

            
