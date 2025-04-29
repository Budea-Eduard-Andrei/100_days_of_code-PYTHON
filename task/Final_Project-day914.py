from random import randint

import art
import game_data
import random

def game():
    final_score = 0
    number1 = random.randint(0,49)
    number2 = random.randint(0,49)
    adv = True
    while adv:
        print(art.logo)
        print(f"Your current score is: {final_score}")
        number = random.randint(0, 49)
        print(f"Compare A: {game_data.data[number1]["name"]}, a {game_data.data[number1]["description"]}, from {game_data.data[number1]["country"]}.")
        print(art.vs)
        print(f"Against B: {game_data.data[number2]["name"]}, a {game_data.data[number2]["description"]}, from {game_data.data[number2]["country"]}.\n")
        print(game_data.data[number1]["follower_count"])
        print(game_data.data[number2]["follower_count"])
        choice = input("Who has more followers? Type 'A' or 'B'.").lower()

        while number2 == number1:
            number2 = random.randint(0, 49)

        if choice == "a" and game_data.data[number1]["follower_count"] < game_data.data[number2]["follower_count"]:
            print(f"\nSorry, that's wrong. Your final score is {final_score}")
            adv = False
        elif choice == "a" and game_data.data[number1]["follower_count"] > game_data.data[number2]["follower_count"]:
            final_score += 1
            number2 = random.randint(0, 49)
        elif choice == "b"  and game_data.data[number1]["follower_count"] > game_data.data[number2]["follower_count"]:
            print(f"\nSorry, that's wrong. Your final score is {final_score}")
            adv = False
        elif choice == "b"  and game_data.data[number1]["follower_count"] < game_data.data[number2]["follower_count"]:
            final_score += 1
            number1 = number2
            number2 = random.randint(0, 49)
        elif game_data.data[number1]["follower_count"] == game_data.data[number2]["follower_count"]:
            print("It's a tie! Moving on...")
            number1 = number2
            number2 = random.randint(0, 49)
            while number2 == number1:
                number2 = random.randint(0, 49)

game()
final_question = input("\nDo you want to play another game? Type 'yes' or 'no'").lower()
while final_question == "yes":
    print("\n" * 200)
    game()
    final_question = input("\nDo you want to play another game? Type 'yes' or 'no'").lower()
print("Thanks for playing!")
