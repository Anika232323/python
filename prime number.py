n=int(input("Enter the number for finding prime number"))
if n<2:
    flag=False
if n==2:
    flag=True
if n>2:
    for i in range(2,n):
        if n%i==0:
            flag=False
            break
        else:
            flag=True
if flag:
    print("The number is prime")
else:
    print("The number is not prime")
