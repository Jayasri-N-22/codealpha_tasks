"""
Task 1: Hangman Game
"""

import random
words=["apple","python","laptop","coding","school"]

word=random.choice(words)
guessed_word=["_"]*len(word)

wrong_guesses= 0
guessed_letters=[]

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while wrong_guesses<6 and "_" in guessed_word:
    
    print("\nWord:", "".join(guessed_word))
    print("Wrong guesses:",wrong_guesses,"/6")

    letter=input("Enter a letter: ").lower()

    if letter in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(letter)
    if letter in word:
        print("Correct!")

        for i in range (len(word)):
            if word[i]==letter:
                guessed_word[i]=letter
    else:
        wrong_guesses+=1
        print("Wrong guess!")

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:",word)
else:
    print("\nGame Over!")
    print("The word was:",word)
