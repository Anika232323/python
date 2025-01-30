#1
class Customer:
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number
    def display_customer(self):
        print("Details of customer","-"*40)
        print(f"Customer Name: {self.name} Customer Phone Number: {self.phone_number}")

class Depositor(Customer):
    def __init__(self,name,phone_number,accno,balance):
        Customer.__init__(self,name,phone_number)
        self.accno=accno
        self.balance=balance
    def display_depositor(self):
        print(f"Customer A/C N0. : {self.accno} Balance : {self.balance}","-"*40)

class Borrower(Depositor):
    def __init__(self,name,phone_number,accno,balance,loan_no,loan_amt):
        Depositor.__init__(self,name,phone_number,accno,balance)
        self.loan_no=loan_no
        self.loan_amt=loan_amt
    def display_borrower(self):
        self.display_customer()
        self.display_depositor()
        print(f"Loan No: {self.loan_no}\nLoan Amount: {self.loan_amt}","-"*40)
customers=[]
n=int(input("Enter the number of customers details you want to add: "))
for i in range(n):
    print()
    name=input("Enter Customer Name :")
    phone_number=int(input("Enter Customer Phone.No :"))
    accno=int(input("Enter Customer A/C No :"))
    balance=float(input("Enter Balance :"))
    loan_no=int(input("Enter Loan number :"))
    loan_amt=float(input("Enter Loan Amount :"))
    print("*"*70)
    customers.append(Borrower(name,phone_number,accno,balance,loan_no,loan_amt))
print("-"*70)
for i in customers:
    i.display_borrower()
    
#2
def longest_good_subarray(nums):
    count = 0
    max_len = 0
    table = {0: 0}
    for i, num in enumerate(nums):
        if num == 0:
            count -= 1
        else:
            count += 1
        if count in table:
            max_len = max(max_len, i - table[count]+1)
        else:
            table[count] = i+1
    return max_len
print(longest_good_subarray([0, 1, 0, 1, 1, 0, 1, 0]))
