import random
from random import randint

number = randint(1,100)
print("Welcome to the Numbers Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' for 10 lives or 'hard' for 5 lives: ").lower()

if difficulty == "easy":
    lives = 9
else:
    lives = 4

def mesaje(variabila, ghicit):
    print(f"You have {variabila + 1} attempts remaining to guess the number.")
    ghicit = int(input("Make a guess: "))
    return ghicit

guess = 0
adv = True
while adv:
    guess = mesaje(variabila=lives, ghicit=guess)

    if lives == 0:
        print("\nYou ran out of lives! You lose!")
        print(f"The number was {number}.")
        exit()

    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        adv = False
    lives -= 1

print(f"\nThe number was {guess}! You won!")