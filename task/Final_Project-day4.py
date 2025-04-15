rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
import sys
alegere = int(input("Come and play rock, paper, scissors. Type 0 for rock, 1 for paper or 2 for scissors\n"))
npc = random.choice([rock,paper,scissors])

if alegere > 2 or alegere < 0:
    print("Wrong inputs")
    sys.exit()

print("You chose:")
if alegere == 0:
    print(rock)
elif alegere == 1:
    print(paper)
else:
    print(scissors)

print("The computer chose:")
print(npc)
if alegere == 0:
    if npc == rock:
        print("Draw")
    elif npc == paper:
        print("You lose")
    else:
        print("You win")
elif alegere == 1:
    if npc == rock:
        print("You win!")
    elif npc == paper:
        print("Draw")
    else:
        print("You lose!")
else:
    if npc == rock:
        print("You lose!")
    elif npc == paper:
        print("You win!")
    else:
        print("Draw")
