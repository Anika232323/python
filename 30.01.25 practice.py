#1
'''n = 5
for i in range(1, n + 1):
    for j in range(1,i+1):
        print(i,end=" ")
        i+=n-j
    print()

#2
n=int(input())
arr =[]
most=[]
for i in range(n):
    arr.append(int(input()))
for i in arr:
    if arr.count(i)<(n/2):
        continue
    else:
        most.append(i)
print(arr)
if len(most)==0:
    print("No element has count greater than n/2 times")
else:
    print(most[0])'''

#3
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.mark={}
    def add_mark(self,subject,mark):
        self.mark[subject]=mark
    def avg_mark(self):
        return sum(self.mark.values())/len(self.mark)
def find_topper(students):
    topper=students[0]
    for student in students:
        if student.avg_mark()>topper.avg_mark():
            topper=student
            return topper
s1 = Student("Bob", 102)
s1.add_mark("Math", 80)
s1.add_mark("Science", 90)
s1.add_mark("English", 85)

s2= Student("Charlie", 103)
s2.add_mark("Math", 93)
s2.add_mark("Science", 90)
s2.add_mark("English", 90)

students=[s1,s2]
topper=find_topper(students)
print(f"Topper: {topper.name}, Roll No: {topper.rollno}, Average Marks: {topper.avg_mark():.2f}")

'''#4
def product_info(name="Laptop", brand="Dell", price=80000, discount=10):
    print("name:",name)
    print("brand:",brand)
    print("price:",price)
    print(f"discount: {discount}%")
    if discount==0:
        print("No discount available")
    else:
        temp=price*(10/100)
        final=int(price-temp)
        print("Final price after discount:",final)
product_info()'''
