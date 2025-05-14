flowerbed=list(map(int,input("Enter flowerbed (space-seperated 0s and 1s):").split()))
n=int(input("Enter number of flowers to plant:"))
count=0
for i in range(len(flowerbed)):
    if (flowerbed[i]==0) and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
        flowerbed[i]=1
        count+=1
    if count>=n:
        print("True")
        break
else:
    print("False")
               
               
