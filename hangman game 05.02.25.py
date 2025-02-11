import random
word_list=["ocean","space","diamond","computer","library","kitten","basketball","pineapple","guitar",
"snowflake",
"perfume",
"llama",
"banana",
"football",
"butterfly",
"coffee",
"bicycle",
"whale",
"dragon",
"starfish",
"grapes",
"piano",
"fountain",
"snowman",
"peacock",
"caramel",
"sunshine",
"tornado",
"fireworks",
"laughter",
"corgi",
"harmonica",
"bicycle",
"fountain",
"parakeet",
"fiddle",
"chocolate",
"lollipop",
"kite",
"submarine",
"peanuts",
"harmonica",
"starlight",
"rainbow",
"giraffe",
"coconut",
"tuya",
"magnolia",
"honeybee"]
guessed_letters=[]
guesses_left=26
word_to_guess=random.choice(word_list)
word_length=len(word_to_guess)
hidden_word=list("_"*word_length)
while guesses_left>0:
    print(f"\nYou have {guesses_left} guesses left.")
    print(f"The word is {' '.join(hidden_word)}")
    print(f"You have guessed: {', '.join(guessed_letters)}")
    guess=input("Enter a letter:").lower()
    if guess in word_to_guess:
        indices=[i for i,x in enumerate(word_to_guess) if x==guess]
        for index in indices:
            hidden_word[index]=guess
        if "_" not in hidden_word:
            print("\nCongratulations! You guessed the word!")
            print(hidden_word)
            break
    else:
        guesses_left-=1
        if guesses_left==0:
            print("\nYou ran out of guesses")
            print(f"The word was {word_to_guess}")
            break
    guessed_letters.append(guess)
