length=int(input("Enter the length of the rectangle:"))
breadth=int(input("Enter the breadth of the rectangle:"))
r_area=length*breadth
print(f"Area of the rectangle is {r_area}")

side=int(input("Enter the side of the square:"))
s_area=side**2
print(f"Area of the square is {s_area}")

radius=int(input("Enter the radius of the circle:"))
c_area=3.14*(radius**2)
print(f"Area of the circle is {c_area}")

base=int(input("Enter the base of the triangle:"))
height=int(input("Enter the height of the triangle:"))
t_area=0.5*base*height
print(f"Area of the triangle is {t_area}")

#fibonacci series
a=0
b=1
n=int(input("Enter the number:"))
print(a)
print(b)
for i in range(n):
    c=a+b
    a=b
    b=c
    print(c)
