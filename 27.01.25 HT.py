#1
def details():
    while True:
        name=input("Enter your name:")
        if not name.isalpha() or name in "!@#$%^&*_":
            print("Username should contain only letters and should not have any special characters")
            continue
        dep=input("Enter your Department:")
        password=input("Enter your password:")
        if not any(i.isdigit() for i in password) or not any(i in "!@#$%^&*_" for i in password) or len(password)<=8:
            print("Password must be 8 characters or less, with at least one number and one special character. Try again")
            continue
        retype=input("Re-Type your Password: ")
        if password!=retype:
            print("Passwords does not match.Try again")
            continue
        encoded_name="X"*len(name)
        encoded_dep="X"*len(dep)
        encoded_pass="X"*len(password)
        encoded_retype="X"*len(retype)
        print(f"Your Encoded Name is: {encoded_name}")
        print(f"Your Department is: {encoded_dep}")
        print(f"Your Password is: {encoded_pass}")
        print(f"Re-Type your Password: {encoded_retype}")
details()

#2
n=int(input("Enter the number of elements:"))
arr=[]
for i in range(n):
    arr.append(int(input()))
print("Original array:",arr)
arr.remove(3)
print("New array:",arr)

#3
n=int(input("Enter the input size:"))
arr=[]
for i in range(n):
    arr.append(input())
print('Your Inverse order Array is:',arr[::-1])
print('Your Non-Inverse order Array is:',arr)




