#string reverse
def reverse(n):
    length=0
    rev=""
    for i in n:
        length+=1
    for  i in range(length-1,-1,-1):
        rev+=n[i]
    return rev
n=input("Enter a string:").strip()
print("The reversed string is:",reverse(n))

#replace the letter in a given string
string=input("Enter a string").strip()
to_replace=input("Enter a string to replace:")
replace_with=input("Enter a character to replace with:")
new=""
for i in string:
    if i==to_replace:
        new+=replace_with
    else:
        new+=i
print(new)
