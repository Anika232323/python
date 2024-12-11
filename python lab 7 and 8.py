#1
sentence=input()
upper=0
lower=0
for i in sentence:
    if i.isupper():
        upper+=1
    if i.islower():
        lower+=1
print("No. of upper letter:",upper)
print("No. of lower letter:",lower)

#2 Palindrome
string=input()
reverse=string[::-1]
print("Reversed string is",reverse)
if reverse==string:
    print("Palindrome")
else:
    print("Not a Palindrome")

    
    
