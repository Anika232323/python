n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print(arr)
n=0
for i in range(len(arr)):
    if arr[i]==0:
        arr[n],arr[i]=arr[i],arr[n]
        n+=1
print(arr)

