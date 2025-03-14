n=int(input("Enter the Number: "))
mid=n//2
for i in range(1,n+1):
    if i<=mid+1:
        spaces_before=i-1
    else:
        spaces_before=n-i
    print(' '*spaces_before,end='')
    print(i,end='')
    spaces_between=(n-2*spaces_before-2)
    if spaces_between>=0:
        print(' '*spaces_between,end='  ')
        print(i,end='')
    print()
