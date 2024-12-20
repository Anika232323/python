password=input()
count=0
for i in password:
    if i.isupper():
        count+=1
if len(password)==12:
    if any(k.islower() for k in password):
        if not password.isdigit():
            if password not in "#!@$%^&":
                if count==3:
                    print("Valid")
                else:
                    print("Invalid")
                    print("Uppercase count should be 3")
            else:
                print("Invalid")
                print("Password should not contain special characters")
        else:
            print("Invalid")
            print("Password should not have digits in it")
    else:
        print("Invalid")
        print("Atleast 1 lower letter should be in password")
else:
    print("Invalid")
    print("Password should have exactly 12 characters")
