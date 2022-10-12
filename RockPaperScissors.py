import random

# sled promqnata
# oshte edna promqna

choices = ["Rock", "Paper", "Scissors"]

player_choice = " "

while True:
    print(" ")
    print("type end/End, to close the game...")
    print(" ")
    player_choice_input = input("Choose: [r]ock, [p]aper, [s]cissors: ")

    # computer randomly chooses between rock paper and scissors
    computer_choice = random.choice(choices)

    if player_choice_input == "End" or player_choice_input == "end":
        print("The game is over!")
        break
    elif player_choice_input != "r" and player_choice_input != "p" and player_choice_input != "s":
        print("Wrong choice, choose between: [r]ock, [p]aper, [s]cissors")
        continue
    else:
        # we set player variable = to the input he gave
        if player_choice_input == "r":
            player_choice = choices[0]
        elif player_choice_input == "p":
            player_choice = choices[1]
        elif player_choice_input == "s":
            player_choice = choices[2]

        print(f"You choose: {player_choice}")
        print(" ")
        print(f"Computer choose: {computer_choice}")
        print(" ")

        # we compare player choice to computer choice
        if player_choice == computer_choice:
            print("It's a DRAW!")
        elif player_choice == choices[0] and computer_choice == choices[2]:
            print("YOU WIN!")
        elif player_choice == choices[0] and computer_choice == choices[1]:
            print("YOU LOSE!")
        elif player_choice == choices[1] and computer_choice == choices[2]:
            print("YOU LOSE!")
        elif player_choice == choices[1] and computer_choice == choices[0]:
            print("YOU WIN!")
        elif player_choice == choices[2] and computer_choice == choices[0]:
            print("YOU LOSE!")
        elif player_choice == choices[2] and computer_choice == choices[1]:
            print("YOU WIN!")
