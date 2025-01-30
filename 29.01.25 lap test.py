#1
dict1={"a":2,"b":4,"c":6}
sum_dict=0
for i in dict1.values():
    sum_dict+=i
print("Sum of elements of the dictionary:",sum_dict)


#2
n=int(input("Enter number:"))
for i in range(1,n+1):
    for  j in range(1,i+1):
        print(i,end=" ")
    print()
