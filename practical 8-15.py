#8 palindrome
n=input("enter string:")
s=n[::-1]
if s==n:
    print('palindrome')
else:
    print('not palindrome')

#9 sum of dict
dict1={'a':1,'b':2,'c':3}
sum_dict=0
for i in dict1.values():
    sum_dict+=i
print(sum_dict)

#10 pattern
n=int(input("Enter a number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#11 file
f1=open('file1.txt','r')
f2=open('file2.txt','w')
cont=f1.readlines()
for i in range(0,len(cont)):
    if (i%2==0):
        f2.write(cont[i])
    else:
        pass
f2.close()
f2=open('file2.txt','r')
cont1=f2.read()
print(cont1)
f1.close()
f2.close()

#12 turtle
import turtle
area=turtle.Screen()
area.setup(width=700,height=550)
turtle.exitonclick()

#13 hangman
import random
word_list=['cat','dog','tiger','lion']
guessed_letters=[]
guesses_left=6
word_to_guess=random.choice(word_list)
word_length=len(word_to_guess)
hidden_word=list('_'*word_length)
while guesses_left>0:
    print(f'You have {guesses_left} guesses left')
    print(f'The word is {' '.join(hidden_word)}')
    print(f'You have guessed {', '.join(guessed_letters)}')
    guess=input("enter your guess:")
    if guess in word_to_guess:
        indices=[i for i,x in enumerate(word_to_guess) if x==guess]
        for index in indices:
            hidden_word[index]=guess
        if "_" not in hidden_word:
            print("Congrats")
            print(hidden_word)
            break
    else:
        guesses_left-=1
        if guesses_left==0:
            print("U lose")
            print(f"The word is {word_to_guess}")
            break
    guessed_letters.append(guess)

#14 json module
import json
from difflib from get_close_matches
data=json.load(open("dict.json"))
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())>0:
             yn=input("Did u mean s% instead? enter y is yes or n if no"%get_close_matches(w,data.keys()[0])
             
