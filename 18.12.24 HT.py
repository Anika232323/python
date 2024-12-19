QUESTION 1:
class Calculator:
    def calc(self,a,b=0,c=0):
        if b==0 and c==0:
            return a**2
        elif c==0:
            return a+b
        else:
            return a*b*c
c=Calculator()
print(c.calc(4))
print(c.calc(2,5))
print(c.calc(2,3,4))
