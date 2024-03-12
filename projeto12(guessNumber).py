import random
import os
def guessing():
    number = random.randint(1,100)
    dificult = input("Chose a dificult. Type 'easy', 'hard' or 'impossible': ").lower()
    if dificult == "hard" :
        attempts = 5
    elif dificult == "easy":
        attempts = 10
    else:
        attempts = 1
    i = 0
    while i < attempts:
        print(f"You have {attempts} attempts remaing to guess the number")
        newAttempt = int(input("Make a guess: "))
        if newAttempt == number:
            print("Correct! You Win!")
            return
        elif newAttempt > number:
            print("Too High.")
            print("Guess Again.")
            attempts -= 1
        else:
            print("Too Low.")
            print("Guess Again.")
            attempts -= 1
    print("No more Guesses! :(")
    print(f"The number was {number}")

print("Welcome to the Number Guessing Game!")
print("I'm thining of a number between 1 and 100.")
stop = False
while not stop:
 guessing()
 again = input("Play Again? y/n: ").lower()
 if again == "n":
     stop = True
 os.system('cls')


