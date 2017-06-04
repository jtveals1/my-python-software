

import random

def main():
    user = input('enter rock paper or scissors')
    computer = generateMove()
    winner = calcWinner(user, computer)
    print("You picked", user, "and the computer picked", computer)
    print(winner, "WINS!")

def generateMove():
    # Generate the computer's move using random.randInt().  
    # This function should return "rock", "paper", or "scissors"
    random_number = random.randint(0,2)
    if random_number == 0:
        computer_choice = "scissors"
    elif random_number == 1:
        computer_choice = "rock"
    elif random_number == 2:
        computer_choice = "paper"
    return computer_choice

def calcWinner (move1, move2):
    # Compares the two moves and returns the winner. 
    # This function should return move1 or move2.  Return move1 if it is a tie
    if move1 == "scissors" and move2 == "scissors":
        winning_move = move1
    elif move1 == "scissors" and move2 == "paper":
        winning_move = move1
    elif move1 == "scissors" and move2 == "rock":
        winning_move = move2
    elif move1 == "rock" and move2 == "rock":
        winning_move = move1
    elif move1 == "rock" and move2 == "paper":
        winning_move = move2
    elif move1 == "rock" and move2 == "scissors":
        winning_move = move1
    elif move1 == "paper" and move2 == "paper":
        winning_move = move1
    elif move1 == "paper" and move2 == "rock":
        winning_move = move1
    elif move1 == "paper" and move2 == "scissors":
        winning_move = move2
    return winning_move

main()
