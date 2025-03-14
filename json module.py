import json
from difflib import get_close_matches
data=json.load(open("dict.json"))
def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("Did u mean %s instead? Enter y if yes or n if no:" %get_close_matches(w,data.keys())[0])
        yn=yn.lower()
        if yn=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="n":
            return "check"
        else:
            return "check"
    else:
        return "check"

word=input("Enter the word:")
output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
input("Press enter to exit")
