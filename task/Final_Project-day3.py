print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You are at a crossroad, where do you want to go? Type left or right\n" ).lower()

if choice1 == "right":
    choice2 = input("You are now at a lake. You have two choices. "
                    "Swim over or wait for a boat to rescue you.  Type swim or wait\n").lower()
    if choice2 == "wait":
        choice3 = input("You got to the other side of the lake and you see 3 X spots. "
                        "Which one do you choose? Type 1, 2 or 3 \n").lower()
        if choice3 == 1:

            input("Congrats! You found the Treasure!")
        else:
            input("You didn\'t guessed the right one. Pyrats are here. RUUN!")
    else:
        input("You\'re not a really good swimer...")
else:
    input("You fell into a hole!")
