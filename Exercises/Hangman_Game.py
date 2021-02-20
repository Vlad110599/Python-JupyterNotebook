#A Simple Hangman Game
import random

with open("wordlist.txt", 'r') as f:
    words = f.readlines()

word = random.choice(words)[:-1]

errors = 7
guesses =[]
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Allowed Errors Left {errors}, Next Guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        errors = errors - 1
        if errors == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"You Win! You found the word: {word}")
else:
    print(f"Game Over! The word was: {word}")