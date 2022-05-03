import random
choices = ["Rock", "Paper", "Scissors"]
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock,Paper or Scissors ?").capitalize()
    computer = random.choice(choices)
    if player == "computer":
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose !", computer, "covers", player)
        else:
            print("You Win!", player, "Smashes", computer)
            player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose !", computer, "cut", player)
            cpu_score += 1
        else:
            print("You Win!", player, "Covers", computer)
            player_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
            cpu_score += 1
        else:
            print("You Win!", player, "cut", computer)
            player_score += 1
    elif player == "End":
        print("Final Scores:")
        print(f"Computer Score:{cpu_score}")
        print(f"Player Score:{player_score}")
        break
