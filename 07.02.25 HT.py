#1
def english_words(n):
    ones=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    teens=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    tens=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    if n==0:
        return "Zero"
    elif n<10:
        return ones[n]
    elif n>=10 and n<=19:
        return teens[n-10]
    elif n<100:
        return tens[n//10]+ones[n%10]
    elif n<1000:
        return f"{ones[n//100]} Hundred {tens[(n%100)//10]} {ones[(n%100)%10]}"
    elif n<10000:
        return f"{ones[n//1000]}Thousand {ones[(n%1000)//100]} Hundred {tens[(n%100)//10]} {ones[(n%100)%10]}"
    elif n>10000:
        return "Number too large"
n=int(input("Enter a number:"))
print(english_words(n))

#2
import math
n1=int(input("Enter a number:"))
fact=math.factorial(n1)
count=0
for i in str(fact):
    if i=="0":
        count+=1
print(count)
