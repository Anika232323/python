class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def check_num(self):
        if not isinstance(num1,int) or not isinstance(num2,int):
            raise ValueError("Non-numeric input not allowed, Try again")
        else:
            if choice >4:
                raise KeyError("Invalid operation, Try again")
            else:
                match choice:
                    case 1:
                        result=self.num1+self.num2
                        return result
                    case 2:
                        result= self.num1-self.num2
                        return result
                    case 3:
                        result= self.num1*self.num2
                        return result
                    case 4:
                        if self.num2==0:
                            raise ZeroDivisionError("Dividing by xero is invalid")
                        else:
                            result =self.num1/self.num2
                            return result
                    case _:
                        exit()
try:
    while True:
        print("1)Addition \n2)Subtraction \n3)Multiplication\n4)Division")
        choice=int(input("Enter the operation number:"))
        num1=int(input("Enter num1:"))
        num2=int(input("Enter num2:"))
        c=Calculator(num1,num2)
        result=c.check_num()
        print(result)
except ValueError as e:
    print(e)
except KeyError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
