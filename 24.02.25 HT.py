
n1=int(input("Enter the start of the range:"))
n2=int(input("Enter the end of the range:"))
lst=[]
pairs=[]
for num in range(n1,n2+1):
    flag=True
    if num>1:
        for i in range(2,int(num**0.5+1)):
            if num%i==0:
                flag=False
                break
        if flag==True:
            lst.append(num)
for i in range(len(lst)-1):
    if lst[i+1]-lst[i]==2:
        pairs.append((lst[i],lst[i+1]))
print(pairs)
