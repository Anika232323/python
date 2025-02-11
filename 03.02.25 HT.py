'''#i. 1.
stu={"Anika":95,"Janu":87,"Dharshini":92,"Kiruthiga":99}
sort=sorted(stu.items(),key=lambda k:k[1])
print(dict(sort))
#i. 2.
stu={"Anika":95,"Janu":87,"Dharshini":92,"Kiruthiga":99}
sort=sorted(stu.items(),key=lambda k:k[1],reverse=True)
print(dict(sort))
#i. 3.
stu={"Anika":95,"Janu":87,"Dharshini":92,"Kiruthiga":99}
sort=sorted(stu.items(),key=lambda k:k[1],reverse=True)
print("Top 3 students are:",dict(sort[:3]))
#i. 4.
stu={"Anika":95,"Janu":87,"Dharshini":92,"Kiruthiga":99}
sort=sorted(stu.items(),key=lambda k:k[0])
print(dict(sort))'''

#ii. 1.
t=(("Joe",50),("Roy",76),("Henry",56),("Nick",90))
sort=sorted(t,key=lambda k:k[1])
print(tuple(sort))
#ii. 2.
t=(("Joe",50),("Roy",76),("Henry",56),("Nick",90))
sort=sorted(t,key=lambda k:k[1],reverse=True)
print(tuple(sort))
#ii. 3.
t=(("Joe",50),("Roy",76),("Henry",56),("Nick",90))
sort=sorted(t,key=lambda k:k[1],reverse=True)
print("Top 3 goal scorers are:",tuple(sort[:3]))
#ii. 4.
t=(("Joe",50),("Roy",76),("Henry",56),("Nick",90))
sort=sorted(t,key=lambda k:k[0])
print(tuple(sort))
