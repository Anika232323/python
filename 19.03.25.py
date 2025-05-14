n = 4
num = 1
for i in range(1,n+1):
    print(" "*(n-i)*6,end="")
    temp=[num+j for j in range(4)]
    num+=4
    if i%2==0:
        temp.reverse()
        print(" ".join(f"{x:2}" for x in temp))
