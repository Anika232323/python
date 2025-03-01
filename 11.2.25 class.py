def hollow_pyramid(n):
    for i in range(1,n+1):
        space="   "*(n-i)
        if i==1:
            print(space+"*")
        elif i==n:
            print(" *"*(2*n-1))
        else:
            print(space+"*"+"   "*(2*i-3)+"*")
n=int(input())
hollow_pyramid(n)
