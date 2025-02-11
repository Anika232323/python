s=input("Enter the input string: ")
longest=""
for i in range(len(s)):
    left,right=i,i
    while left>=0 and right<len(s) and s[left]==s[right]:
        left-=1
        right+=1
    odd_palindrome=s[left+1:right]
    left,right=i,i+1
    while left>=0 and right<len(s) and s[left]==s[right]:
        left-=1
        right+=1
    even_palindrome=s[left+1:right]
    if len(odd_palindrome)>len(longest):
        longest=odd_palindrome
    if len(even_palindrome)>len(longest):
        longest=even_palindrome
print(longest)
