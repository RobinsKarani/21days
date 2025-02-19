import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_pick = input("Game loading ...\nType rock/paper/scissors or Q to quit: ").lower()

    if user_pick == "q":
        break

    if user_pick not in options:
        print("Invalid input. Please try again.")
        continue

    #Randomly pick for the computer
    computer_pick = random.choice(options)
    print(f"Computer picked {computer_pick}.")

    if computer_pick == "rock" and user_pick == "scissors":
        print("You win!")
        user_wins += 1
    elif computer_pick == "paper" and user_pick == "rock":
        print("You win!")
        user_wins += 1
    elif computer_pick == "scissors" and user_pick == "paper":
        print("You win!")
        user_wins += 1
    elif computer_pick == user_pick:
        print("It's a tie! Try again.")
    else:
        print("Computer wins!")
        computer_wins += 1


print("----Game ended----")
print(f"You won {user_wins} times.")
print(f"The computer won {computer_wins} times.")
