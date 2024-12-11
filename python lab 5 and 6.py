def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter the number:"))
print(f"The factorial of {factorial(num)}")
"""
even=0
odd=0
arr=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    arr.append(int(input()))
print(arr)
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)
"""
    
