def Hanoi(n,start,end,temp):
    if n==1:
        print("Move disk 1 from the rod",start,"to the rod",end)
        return
    Hanoi(n-1,start,end,temp)
    print("Move disk",n,"from the rod",start,"to the rod",end)
    Hanoi(n-1,temp,start,end)
n=int(input("Enter the number:"))
Hanoi(n,'A','B','C')

dict1={'a':2,'b':4,'c':6}
sum_dict=0
for i in dict1.values():
    sum_dict+=i
print(sum_dict)
