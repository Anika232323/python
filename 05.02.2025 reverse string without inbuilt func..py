n=input("Enter a string:").strip()
length=0
for i in n:
    length+=1
for  i in range(length-1,-1,-1):
    print(n[i],end="")
