#1
'''import math
n=int(input("Enter the number of employees:"))
lst=[]
for i in range(1,n+1):
    lst.append(i) #[1,2,3,4]
s=0
for i in lst:
    f=math.factorial(i)
    s+=f
print(s)

#2
def fibonacci(x):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(x+1):
        c=a+b
        a=b
        b=c
        print(c)
        if c>x:
            print(f"First Fibonacci number greater than {x}:",c)
            break
x=int(input("Enter the threshold:"))
fibonacci(x)'''

#3
sentence=input("Enter a sentence:")
words=sentence.split()
n=0
n1=[]
while n<len(words):
    
    n1.append(len(words[n]))
    n+=1
print(n1)
s=sorted(n1)
l=s[-1]
for i in words:
    if len(i)==l:
        print(f"Longest word: '{i}' with length {l}")

    
    
