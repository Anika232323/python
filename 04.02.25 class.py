'''#caps to small
character=input()
if 'A'<=character<='Z':
    c=ord(character)+32
    converted=chr(c)
print(converted)

#small (string) to caps (String)
character=input()
for i in character:
    if 'a'<=i<='z':
        c=ord(i)+32
        converted=chr(c)
    print(converted,end="")

#FUNCTION
def up_low(char):
    p=ord(char)
    c=chr(p+32)
    print(c,end="")

def low_up(char):
    r=ord(char)
    s=chr(r-32)
    print(s,end="")
string=input("Enter a string:")
for i in string:
    if 'A'<=i<='Z':
        up_low(i)
    elif 'a'<=i<='z':
        low_up(i)'''


lst=list(map(str,input().split()))
s=""
for i in lst:
    for j in i:
        if 'a'<=j<='z':
            r=ord(j)
            s+=chr(r-32)
lst2=[]
for i in s:
    lst2.append(i)
print(lst2)
