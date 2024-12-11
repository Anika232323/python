'''QUESTION 1:
class password:
    def __init__(self):
        self.password=input("Enter the password:")
    def valid(self):
        self.length=8
        self.l_count=0
        self.u_count=0
        self.d_count=0
        self.s_count=0
        for i in self.password:
            if i.isupper():
                self.u_count+=1
            if i.islower():
                self.l_count+=1
            if i.isdigit():
                self.d_count+=1
            if not i.isalpha() and not i.isdigit() and not i.isalnum():
                self.s_count+=1
        if self.u_count>=1:  
            if self.l_count>=1:
                if self.d_count>=1:
                    if self.s_count>=1:
                        if  len(self.password)>=self.length:
                            print("valid")
                        else:
                            print("The password should have minimum length of 8 characters.")
                    else:
                        print("The password should have at least one special character.")
                else:
                    print("The password should have at least one digit.")
            else:
                print("The password should have at least one lowercase letter.")
        else:
            print("Invalid password")
            print("The password should have at least one uppercase letter.")
v=password()
v.valid()'''

class TextProcessor:
    def __init__(self,text):
        self.text=text
    def split_into_sentences(self):
        sentences=[]
        sentence=""
        for i in self.text:
            sentence+=i
            if i in "!?.":
                sentences.append(sentence.strip())
                sentence=""
        return sentences
    def process_sentence(self):
        sentences=self.split_into_sentences()
        print("Processed Sentence Data:")
        for sentence in sentences:
            word=len(sentence.split())
            print(f"Sentence: {sentence},Word Count:{word}")
para=input("Enter your paragraph:")
t=TextProcessor(para)
print("Split Sentences")
sentences=t.split_into_sentences()
for sentence in sentences:
    print(f"{sentence}")
t.process_sentence()
        
        
                
        
        

                
        
        
