def single(arr):
    new=[]
    def flatten(element):
        if isinstance(element,list):
            for i in element:
                flatten(i)
        else:
            new.append(element)
    flatten(arr)
    return new
arr=[1,[2,[3,[4,5]],6],7]
print(single(arr))
