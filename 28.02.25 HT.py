n=int(input())
temp=97
let=[]
for i in range(n+1):
    let.append(chr(temp))
    temp+=1
print(let)
for i in range(len(let)-1):
    print(let[i]+let[i+1]+let[i]+let[i+1])
