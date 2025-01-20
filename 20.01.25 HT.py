class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance

    def deposit(self,dep_amt):
        if dep_amt<0:
            return "Deposit amount cannot be negative"
        else:
            self.__balance+=dep_amt
            return "Amount deposited successfully"

    def withdraw(self,with_amt):
        if with_amt<0:
            return "Withdrawal amount cannot be negative"
        else:
            self.__balance-=with_amt
            return "Amount withdrawed successfully"

    def add_interest(self,rate):
        if rate<0:
            return "Rate cannot be negative"
        else:
            interest=self.__balance*(rate/100)
            self.__balance-=interest
            return "Interest added"

    def get_acc_num(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance
account_number=int(input("Enter account number:"))
balance=int(input("Enter initial balance:"))
acc=BankAccount(account_number,balance)
print("1.Deposit\n2.Withdraw\n3.Add interest\n4.Check balance\n5.Exit")
while True:
    choice=int(input("Enter ur choice:"))
    if choice==1:
        dep_amt=int(input("Enter amount to deposit:"))
        print(acc.deposit(dep_amt))
    elif choice==2:
        with_amt=int(input("Enter amount to withdraw:"))
        print(acc.withdraw(with_amt))
    elif choice==3:
        rate=int(input("Enter interes5t rate:"))
        print(acc.add_interest(rate))
    elif choice==4:
        print(acc.get_balance())
    elif choice==5:
        break
    else:
        print("Invalid Input")
