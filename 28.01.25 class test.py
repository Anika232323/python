arr=list(map(int,input("Enter the elements of the array separated by space:").split(" ")))
print("Elements at odd positions:")
for i in range(len(arr)):
    if i%2!=0:
        print(f"Index: {i}, Value: {arr[i]}")
print("Elements at Even positions:")
for i in range(len(arr)):
    if i%2==0:
        print(f"Index: {i}, Value: {arr[i]}")
        
