QUESTION 1:
class Count:
    def __init__(self,in_str):
        self.in_str=in_str
    def count_alphabet(self):
        a_count=0
        for i in self.in_str:
            if i.isalpha():
                a_count+=1
        print("Alphabetic Characters:",a_count)
    def count_num(self):
        n_count=0
        for i in self.in_str:
            if i.isnumeric():
                n_count+=1
        print("Numeric Characters:",n_count)
    def count_special(self):
        s_count=0
        for i in self.in_str:
            if i in"!@#$%^&*()_+-?/.":
                s_count+=1
        print("Special Characters:",s_count)
user=input("Enter a string: ")
c=Count(user)
c.count_alphabet()
c.count_num()
c.count_special()

QUESTION 2:
class Validate:
    def __init__(self,in_str):
        self.in_str=in_str
    def validate_string(self):
        sp="!@#$%^&*()_+-=."
        s_count=0
        a_count=0
        for i in self.in_str:
            if i.isalpha():
                a_count+=1
            if i in sp:
                s_count+=1
        if a_count<1:
            return "String must contain atleast one alphabet"
        if s_count<1:
            return "String must contain atleast one special character"
        return "The string contains both alphabets and special characters."
user=input("Enter a string: ")
v=Validate(user)
print(v.validate_string())
 
