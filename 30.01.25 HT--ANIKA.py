#1
import re
class UserValidation:
    def __init__(self):
        self.name=""
        self.password=""
        self.email=""
        self.print_count=0
    def validate_name(self,name):
        dig_count=0
        spc_count=0
        for i in range(len(name)):
            if name[i].isdigit():
                dig_count+=1
            if name[i] in "!@#$%^&*-_":
                spc_count+=1
        if dig_count==1 and spc_count==1:
            return name
    def validate_password(self,password):
        for i in range(len(password)):
                if password.isalpha() and password not in "!$%^&*-" and len(password)>8:
                    return password
    def validate_email(self,email):
        return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
    def user_input(self):
        while True:
            name=input("Enter your name:")
            if self.validate_name(name):
                self.name=name
                break
            print("Invalid name format. it should contain one number and one special character")

        while True:
            password=input("Enter your password:")
            if self.validate_password(password):
                self.password=password
                break
            print("Invalid password format. It should contain only numbers and special characters")

        while True:
            email=input("Enter your email: ")
            if self.validate_email(email):
                self.email=email
                break
            print("Invalid email format")

        while True:
            try:
                print_count=int(input("How many times do you want to print? "))
                if print_count>0:
                    self.print_count=print_count
                    break
                print("Please enter a positive number..")
            except ValueError:
                print("Invalid Input! Enter a valid number..")
    def print_output(self):
        print(f"{self.name} wants to print {self.print_count} Times and send  Mail to {self.email}.")
        print(f"Your Password {'*' *len(self.password)} will be encrypted and will be stored.")
            
user=UserValidation()
user.user_input()
user.print_output()
            
#2
class Password:
    def init(self):
        self.name=None
        self.dept=None
        self.password=None
        self.security_ques=None

    def validate_password(self,password,re_pass):
        sc="!@#$%^&*()-_.,"
        if len(self.password)>8:
            return "Password should not be greater than 8 in length.."
        if not any(char.isdigit() for char in password):
            return "Password must contain atleast one number.."
        if not any(char in sc for char in password):
            return "Password must contain atleast one special character.."
        if re_pass!=self.password:
            return self.authenticate_password()
            
    def authenticate_password(self):
        attempts = 3
        while attempts > 0:
            enter_password = input("Enter your password: ")
            if enter_password == self.password:
                print("Access granted..")
                
            else:
                print(f"Incorrect Password.. Attempts left: {attempts - 1}")
                attempts -= 1
            if attempts == 0:
                choice = input("\nDo you want to reset your password? (Yes/No): ").strip().lower()
                if choice == "yes":
                    return self.forget_password()  
                else:
                    print("Password reset is not chosen. Exiting.")
                    exit()
    def forget_password(self):
        if not self.security_ques:
            self.security_ques=[("what is your username?",self.name),
                                            ("What is your department?",self.dept)]

        print("Forget password option: ")
        for _ in range(3):
            print("Please answer the security questions: ")
            crct_ans=0
            while True:
                for ques,ans in self.security_ques:
                    answer=input(f"{ques} ")
                    if answer==ans:
                        crct_ans+=1
                    else:
                        print("Incorrect answers.Try again..")
                        break
                if crct_ans==len(self.security_ques):
                    print("security questions answered correctly.")
                    print("\nYour Password is: ",self.password)
                    return True

                
            
    def validate_pass(self):
        while True:
            self.password=input("Enter your password: ")
            retype=input("Re-type your password again: ")
            error=self.validate_password(self.password,retype)
            if error:
                print(error)
            else:
                break
        
    def print_details(self):
        while True:
            self.name=input("Enter your Name: ")
            self.dept=input("Enter your Department: ")
            self.validate_pass()
            result=(
                f"Your Encoded Name is:{'*' *len(self.name)}\n"
                f"Your Department is: {'*' *len(self.dept)}\n"
                f"Your Password is: {'*' *len(self.password)}\n"
                f"Re-Type your Password: {'*' *len(self.password)}\n"
            )
            print(result)


pas=Password()
pas.print_details()
pas.authenticate_password()
if not pas.forget_password():
    print("Authentication failed..")
else:
    print("Authentication successful..")
