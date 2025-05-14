def rearrange_array(arr):
    n = len(arr)
    for i in range(n - 1):
        if (i % 2 == 0 and arr[i] < arr[i + 1]) or (i % 2 == 1 and arr[i] > arr[i + 1]):
            arr[i], arr[i + 1] = arr[i + 1], arr[i] 
    return arr
arr = [5, 3, 1, 2, 3, 7, 6, 4]
result = rearrange_array(arr)
print(result)
