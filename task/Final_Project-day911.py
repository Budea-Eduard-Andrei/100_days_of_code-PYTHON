import art
import random

nr = [11 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

carti_jucator =[]
carti_dealer = []

carti_jucator.append(random.choice(nr))
carti_jucator.append(random.choice(nr))

carti_dealer.append(random.choice(nr))
carti_dealer.append(random.choice(nr))

first_guestion = input("Do you want to play a game of Blackjack? Type 'Yes' or 'No'\n").lower()


def joc():
    print(art.logo)

#BLACKJACK INCEPUT
    total_jucator = 0
    for i in carti_jucator:
        total_jucator += i
    total_dealer = 0
    for i in carti_dealer:
        total_dealer += i

    if total_dealer == 21:
        print(f"Your hand is: {carti_jucator}, your score is: {total_jucator}")
        print(f"Computer's hand is: {carti_dealer}")
        print("Dealer had Blackjack! You lost!")
        exit()
    elif total_jucator == 21:
        print(f"Your hand is: {carti_jucator}, your score is: {total_jucator}")
        print(f"Computer's first card is: {carti_dealer[0]}")
        print("You have Blackjack! You win!")
        exit()

    print(f"Your hand is: {carti_jucator}, your score is: {total_jucator}")
    print(f"Computer's first card is: {carti_dealer[0]}")
    second_question = input("Type 'y' to get another card or 'n' to stay\n").lower()


    while second_question == "y":
        carti_jucator.append(random.choice(nr))
        total_jucator = sum(carti_jucator)
        while total_jucator > 21 and 11 in carti_jucator:
            carti_jucator.remove(11)
            carti_jucator.append(1)
            total_jucator = sum(carti_jucator)

        if total_jucator > 21:
            print(f"Your hand is: {carti_jucator}, final score is {total_jucator}")
            print(f"Computer's hand is: {carti_dealer[0]}")
            print("You BUSTED!")
            break
        elif total_jucator == 21:
            break
        else:
            print(f"Your hand is: {carti_jucator}, final score is {total_jucator}")
            print(f"Computer's hand is: {carti_dealer[0]}")
            second_question = input("Type 'y' to get another card or 'n' to stay\n").lower()

    if second_question == "n" or total_jucator == 21:
        while total_dealer < 17:
            carti_dealer.append(random.choice(nr))
            total_dealer = sum(carti_dealer)

    if total_jucator < 21:
        if total_dealer > 21:
            print(f"Your hand is: {carti_jucator}, final score is {total_jucator}")
            print(f"Computer's hand is: {carti_dealer}, final score is {total_dealer}")
            print("Dealer BUSTED! You win!")
        elif total_dealer == total_jucator:
            print(f"Your hand is: {carti_jucator}, final score is {total_jucator}")
            print(f"Computer's hand is: {carti_dealer}, final score is {total_dealer}")
            print("It's a DRAW!")
        elif total_dealer < total_jucator:
            print(f"Your hand is: {carti_jucator}, final score is {total_jucator}")
            print(f"Computer's hand is: {carti_dealer}, final score is {total_dealer}")
            print("You win !!!")
        else:
            print(f"Your hand is: {carti_jucator}, final score is {total_jucator}")
            print(f"Computer's hand is: {carti_dealer}, final score is {total_dealer}")
            print("You lost ! ")

if first_guestion == "yes":
    joc()
else:
    print("Ok..")

final_question = input("\nDo you want to play another game? Type 'yes' or 'no'\n").lower()
while final_question == "yes":
    print("\n" * 200)

    carti_jucator = []
    carti_dealer = []

    carti_jucator.append(random.choice(nr))
    carti_jucator.append(random.choice(nr))

    carti_dealer.append(random.choice(nr))
    carti_dealer.append(random.choice(nr))

    joc()
    final_question = input("\nDo you want to play another game? Type 'yes' or 'no'\n").lower()




