words=input("Enter words separated by spaces: ").split()
results=[]
for i in range(len(words)):
    for j in range(len(words)):
        if i!=j:
            combined=words[i]+words[j]
            if combined==combined[::-1]:
                results.append([i,j])
print(results)
