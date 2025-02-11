n=int(input("Enter the number for printing the factorial"))
factorial=1
while n>1:
    factorial*=n*(n-1)
    n=n-2
print("The factorial is ",factorial)
