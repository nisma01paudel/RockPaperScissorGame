
import random
moves_list = ["Rock", "Paper", "Scissor"]

user_move = input("Enter your move = Rock, Paper, Scissor= ")
comp_move = random.move(moves_list)

print(f"User move = {user_move}, Computer move = {comp_move}")

if user_move == comp_move:
    print("Both moves same: = Match draw")

elif user_move == "Rock":
    if comp_move == "Paper":
        print("Paper covers Rock = Computer Win")
    else:
        print("Rock crushes Scissor = You win")

elif user_move == "Paper":
    if comp_move == "Scissor":
        print("Scissor cuts paper, Computer Win")
    else:
        print("Paper covers rock, You win")

elif user_move == "Scissor":
    if comp_move == "Paper":
        print("Scissor cuts paper, You win")
    else:
        print("Rock crushes scissor, Computer win")
