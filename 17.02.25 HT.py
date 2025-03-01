#1
def merge_dictionary(dict1,dict2):
    dict1.update(dict2)
    return dict1
dict1={}
n1=int(input("Enter the number of elements for dict1:"))
for i in range(n1):
    key1=input("Enter a key:")
    value1=input("Enter a value:")
    dict1[key1]=value1
dict2={}
n2=int(input("Enter the number of elements for dict2:"))
for i in range(n2):
    key2=input("Enter a key:")
    value2=input("Enter a value:")
    dict1[key2]=value2
print(merge_dictionary(dict1,dict2))

#2
def common_dict():
    for i in lst1:
        if i in lst2:
            dict1[i]=lst1.count(i)
    return dict1
lst1=[1,2,2,1,4]
lst2=[1,3,4,5]
dict1={}
print(common_dict())

#3
def dictionary():
    dict1=dict(lst)
    print(dict1)
lst=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    key=input("Enter the key:")
    val=input("Enter the value:")
    lst.append((key,val))
dictionary()
