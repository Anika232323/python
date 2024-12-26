#question 2:
lst1=[1,5,3,8,6,0]
lst2=[2,5,4,6,7,11]
new=[]
for i in lst1:
    if i in lst2:
        lst1.remove(i)
        lst2.remove(i)
print(lst1)
print(lst2)
lst3=lst1+lst2
print(sorted(lst3))

#question3
num=int(input("Enter number:"))
n=num
sum_of_num=0
while num>0:
    temp=num%10
    sum_of_num+=temp
    num//=10
print(sum_of_num)    

#question 4:
lst1=[2,5,6,1,9]
lst2=[5,6,2,0,3]
common=[]
for i in lst1:
    if i in lst2:
        common.append(i)
print(common)

#question 5:
string=input()
count=0
for i in string:
    if i.isalnum():
        count+=1
print(count)

#question 6:
lst=[56,24,67,42,65,3,54]
new=sorted(lst)
print("Sorted list is:",new)

#question 7:
class BankAccount:
    def __init__(self,Amount):
        self.Amount=Amount
    def deposit(self):
        dep=int(input("Enter amount to deposit:"))
        if dep<0:
            print("Deposit amount cannot be negative")
        else:
            self.Amount=dep+self.Amount
            print("Successfully deposited")
    def withdraw(self):
        withdraw_money=int(input("Enter amount to withdraw:"))
        if withdraw_money>self.Amount:
            print("Insufficient balance")
        else:
            self.Amount=self.Amount-withdraw_money
            print("Successfully withdrawed")
    def check(self):
        print("Your current balance is:",self.Amount)
n=BankAccount(1500)
n.deposit()
n.withdraw()
n.check()

#question 8:
valid="@gmail.com"
email=input("Enter ur email:")
if valid in email:
    print("Valid")
else:
    print("Invalid")
    print("Email should be in the format:@gmail.com")

#question 9:
txt=input("Enter text:")
temp=''
for i in txt:
    if i.isdigit():
        temp+=i
print(temp)

#question 10:
text=input("Enter text:")
temp=[]
for i in text:
    if i=="#":
        temp.append(i)
for i in temp:
    print(i,end="")




