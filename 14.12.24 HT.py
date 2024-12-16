QUESTION 1:
word1="ab"
word2="pqrs"
a=""
i=0
j=0
while i<=len(word1) or j<=len(word2):
    if i<len(word1):
        a+=word1[i]
    i+=1
    if j<len(word2):
        a+=word2[j]
    j+=1
print(a)

QUESTION 2:
flowerbed=list(map(int,input().split()))
n=int(input("Enter how many flowers you needed to plant:"))
count=0
for i in range(len(flowerbed)):
    if flowerbed[i]==0 :
         left=(i==0 or flowerbed[i-1]==0)
         right=(i==len(flowerbed)-1 or flowerbed[i+1])==0
         if left and right:
             flowerbed[i]=1
             count+=1
         if count>=n:
             print("True")
             break
else:
    print("False")
