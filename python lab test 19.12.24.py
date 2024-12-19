#factorial
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter a number:"))
print(f"Factorial of {num} is {factorial(num)}")

#grade
mark1=int(input("Enter mark1:"))
mark2=int(input("Enter mark2:"))
mark3=int(input("Enter mark3:"))
mark4=int(input("Enter mark4:"))
mark5=int(input("Enter mark5:"))
total=mark1+mark2+mark3+mark4+mark5
print("Total mark:",total)
percentage=(total/500)*100
print("Percentage:",percentage)
if percentage>=80:
    print("Grade A")
elif percentage>=70:
    print("Grade B")
elif percentage>=60:
    print("Grade C")
elif percentage>=50:
    print("Grade D")
else:
    print("Grade E")
