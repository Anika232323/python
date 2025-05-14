s = input("Enter the string").lower()
vowels = {'a', 'e', 'i', 'o', 'u'}
n = len(s)
l_s = ""
for i in range(n):
    seen = set()
    v = False
    current_str = ""
    for j in range(i, n):
        if s[j] in seen:
            break
        seen.add(s[j])
        current_str += s[j]
        if s[j] in vowels:
            v = True
        if v and len(current_str) > len(l_s) or len(current_str) == len(l_s) and current_str < l_s:
            l_s = current_str
print(len(l_s))
print(l_s)
