candies=list(map(int,input().split()))
extra=int(input("Enter:"))
greater=max(candies)
op=[]
for j in candies:
    total=j+extra
    if total>=greater:
        op.append("true")
    else:
        op.append("false")
print(op)
