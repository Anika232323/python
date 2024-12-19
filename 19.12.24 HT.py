roman =[(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),(100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),(10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
n=int(input("Enter the number to convert into a roman number"))
result=""
for num,letter in roman:
    while n>=num:
        result+=letter
        n-=num
print("The roman for the given integer is:",result)
