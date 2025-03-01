t=tuple(map(str,input().split()))
prefix=t[0]
if not prefix:
    print(" ")
for i in t[1:]:
    while not i.startswith(prefix):
        prefix=prefix[:-1]
print("Longest Common Prefix in Tuple is: ",prefix)
