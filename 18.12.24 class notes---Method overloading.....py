#Method overloading
#same method name but different parameters
class addition:
    def add(self,a,b,c=0):
        result=0
        result=a+b+c
        return result
ad=addition()
ans=ad.add(2,3)
print(ans)
ans1=ad.add (3,5,6)
print(ans1)

#operator overloading
#We can use same operator for multiple purposes
#eg: the +operator will perform an arithmetic addition operation when use with number
#but with strings it will perform concatenation.

#magic method __add__()
class Book:
    def __init__(self,pages):
        self.pages=pages

    #overloading +operator with magic method
    def __add__(self,other):
        return self.pages+other.pages
b1=Book(400)
b2=Book(300)
print("Total number of page:",b1+b2)
