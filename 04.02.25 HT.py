#1
string=input("Enter a string:")
words=string.split()
count=len(words[-1])
print(f" The last word is '{words[-1]}' with length {count}")

#2
a=input()
b=input()
sum_binary=bin(int(a,2)+int(b,2))[2:]
print(sum_binary)
