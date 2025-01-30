#1
n=int(input("Enter the number of inputs:"))
arr=[]
for i in range(n):
    arr.append(input())
for i in range(n):
    print(f"{arr[i]} - index of array is [{i}]")

#2
n=int(input("Enter the number of inputs:"))
arr=[]
for i in range(n):
    arr.append(input())
user=int(input("Select the index position to remove:"))
arr.remove(arr[user])
print("Array after removing an element is-",arr)

#3
n=int(input("Enter the number of inputs:"))
arr=[]
for i in range(n):
    arr.append(input())
user=int(input("Select the element location to add:"))
new="Global"
arr.insert(user,new)
print(arr)

#4
n=int(input("Enter the number of inputs:"))
arr=[]
for i in range(n):
    arr.append(input())
for i in range(n):
    print(f"{arr[i]} - index of array is [{i}]")
print("Odd position array elements are")
for i in range(n):
    if i%2!=0:
        print(f"{arr[i]} - index of array is [{i}]")
print("Even position array elements are")
for i in range(n):
    if i%2==0:
        print(f"{arr[i]} - index of array is [{i}]")
