n=int(input("Enter the number of rows: "))
sequence=["1"]
row=1
while row<n:
    prev=sequence[-1]
    count=1
    new_seq=""
    i=1
    while i<len(prev):
        if prev[i]==prev[i-1]:
            count+=1
        else:
            new_seq+=str(count)+prev[i-1]
            count=1
        i+=1
    new_seq+=str(count)+prev[-1]
    sequence.append(new_seq)
    row+=1
for row in sequence:
    print(" ".join(row))
