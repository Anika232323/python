#1
'''lst=list(map(int,input().split()))
k=int(input("Enter the kth value:"))
rev_lst=sorted(lst,reverse=True)
print(rev_lst[k-1])

#2
num=int(input("Enter a number:"))
temp=str(num)
sum_num=0
for i in range(1,len(temp)+1):
    sum_num+=int(temp[i-1])**i
if sum_num==num:
    print("Disarium number")
else:
    print("Not a disarium number")'''


lst=list(map(int,input().split())) #6 2 4 5 7
n = len(lst) # 5
k=int(input("Enter the kth value:")) 
for i in range(n): # 0,1,2,3,4
    for j in range(0, n-i-1): # 0,4
        if lst[j]<lst[j+1]: #
            lst[j], lst[j+1] =lst[j+1],lst[j]
print(lst) # 7 6 5 4 2
print(lst[k-1])



