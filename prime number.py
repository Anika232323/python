n1=int(input())
n2=int(input())
flag=True
lst=[]
pairs=[]
for num in range(n1,n2+1):
    if num>2:
        for i in range(2,n1):
            if num%i==0:
                flag=False
                break
        else:
            flag=True
    if flag:
        lst.append(num)

for i in range(len(lst)-1):
    pairs.append((lst[i],lst[i+1]))
print(pairs)
