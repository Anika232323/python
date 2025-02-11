#lambda arguments:expression
'''add=lambda a,b:a+b
print(add(1,2))

add=lambda a,b,c:a+b+c
print(add(1,2,3))

#square each element in the list
lst=list(map(int,input().split()))
sq=map(lambda s:s**2,lst)
print(list(sq))

#filter even numbers in a list
lst1=list(map(int,input().split()))
even=filter(lambda x:x%2==0,lst1)
print(list(even))

#sorts the list based on the first element
t=[(1,2),(6,3),(4,1)]
t1=sorted(t,key=lambda x:x[0])
print(t1)'''

name=["ani","jan","shri"]
salary=[65000,50000,70000]
phno=[8939219826,9839327493,8939119916]
data=zip(name,salary,phno)
print(data)
sort=sorted(data,key=lambda k:k[0])
print(sort)
