#1
def common(string):
    if not string:
        return""
    prefix=string[0]
    for i in string[1:]:
        while not i.startswith(prefix):
            prefix=prefix[:-1]
            if not prefix:
                return "''"
    return prefix
print("The longest common prefix in the string is: ",common(["flower", "flow", "flight"]))
print("The longest common prefix in the string is: ",common(["dog", "racecar", "car"]))

#2
def is_subsequence(s,t):
    m=len(s)
    n=len(t)
    i=0
    j=0
    while i<m and j<n:
        if s[i]==t[j]:
            i+=1
        j+=1
    return i==m
s=input("Enter the subsequence string: ")
t=input("Enter the main string: ")
print(is_subsequence(s,t))
