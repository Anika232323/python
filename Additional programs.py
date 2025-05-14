
#1 Armstrong
n=int(input("Enter any number:"))
user=n
temp=n
digits=[]
count=0
while n>0:
    dig=temp%10
    digits.append(dig)
    count+=1
    temp//=10
    n//=10
armstrong=0
for i in digits:
    armstrong+=(i**count)
if user==armstrong:
    print("Armstrong")
else:
    print("Not an armstrong")

#2 leap year or not
year=int(input("Enter the year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:
            print("Not a leap year")
    else:
            print("leap year")
else:
            print("Not a leap year")

#3 Matrix multiplication
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = [[0, 0], [0, 0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

print("Matrix A:")
for row in A:
    print(row)
print("Matrix B:")
for row in B:
    print(row)
print("Matrix A x B:")
for row in C:
    print(row)

#4 turtle
import turtle
screen=turtle.Screen()
screen.bgcolor('lightblue')
screen.setup(700,550)
turtle.exitonclick()

#5 calender
import calendar
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
print(calendar.month(year, month))

#6 turtle-star
import turtle
screen = turtle.Screen()
screen.bgcolor("light blue")
star = turtle.Turtle()
for i in range(5):
    star.forward(100) 
    star.right(144)
turtle.exitonclick()

#7 matrix addition
rows=int(input("Enter number of rows:"))
cols=int(input("Enter number of columns:"))
A=[]
print("Enter first matrix:")
for i in range(rows):
    A.append(list(map(int,input().split())))
print("Enter second matrix:")
B=[]
for i in range(rows):
    B.append(list(map(int,input().split())))
result=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(A[i][j]+B[i][j])
    result.append(row)
for row in result:
    print(' '.join(map(str,row)))
