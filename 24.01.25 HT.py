#1
first_name=input("Enter your first name:")
last_name=input("Enter your last name:")
clg_name=input("Enter your college name:")
stream=input("Enter your stream:")
num=input("Enter your mobile number:")
name=first_name+last_name
dep=clg_name+stream
as_name=[]
as_num=[]
print(f"Your Name is : {name}")
print(f"Your College Name : {dep}")
print("Your ASCII value of name is:")
for i in name:
    if i!="":
        as_name.append(ord(i))
    print(f"{i}-{ord(i)}")
print("Your ASCII value of mobile number is:")
for i in num:
    if i!="":
        as_num.append(ord(i))
    print(f"{i}-{ord(i)}")
n=0
print("Results of addition:")
for i in name:
    print(f"{i}+{num[n]}={as_name[n]+as_num[n]}")
    n+=1

#2
p = int(input("Enter the first value: "))
q = int(input("Enter the second value: "))
r = int(input("Enter the third value: "))
add = p +q
sub= p - q
mul=p * q
div= p/q
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")
print("\nBefore Swapping:")
print(f"First value: {p}")
print(f"Second value: {q}")
print(f"Third value: {r}")
p = r
q=p
r=q
print("\nAfter Swapping:")
print(f"First value: {p}")
print(f"Second value: {q}")
print(f"Third value: {r}")

#3
username=input("Enter first name:")
filtered_name=""
for char in username:
    if not char.isdigit():
        filtered_name+=char
print("Hi!!! Your entered input is:",filtered_name)
print()
username=input("Enter first name:")
characters=""
spl_chars=""
for char in username:
    if char.isalpha():
        characters+=char
    elif not char.isdigit():
        spl_chars+=char
print("Your entered characters are:",characters)
print("Your entered special characters are:",spl_chars)      
