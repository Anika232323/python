rows=int(input("Rows"))
cols=int(input("Columns"))
A=[]
print("first matrix")
for i in range(rows):
    A.append(list(map(int,input().split())))
B=[]
print("second matrix")

for i in range(rows):
    B.append(list(map(int,input().split())))
result=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(A[i][j]+B[i][j])
    result.append(row)
for row in result:
    print(" ".join(map(str,row)))
