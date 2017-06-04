# Complete the following program by writing the generateMove() and calcWinner() functions 
#      paper wraps rock  -- paper wins
#      scissors cut paper -- scissors win
#      rock breaks scissors -- rock wins
#
# Example program output:
#
#    Enter rock, paper, or scissors:  rock
#    You picked rock and the computer picked scissors
#    rock WINS!
#
# Add your name and date to the header comment, and delete these instructions.



# Rock Paper Scissors Game
# Author: Jason Veals
# Date: 6-13-2016

import random

PAPER    = "paper"
ROCK     = "rock"
SCISSORS = "scissors"

def main():

    userMove = validateMove()
    compMove = generateMove()
    winner = calcWinner(userMove, compMove)
    print("You picked", userMove, "and the computer picked", compMove)
    print(winner, "WINS!")

#Validates user's move
def validateMove():
    userMove = "NULL"
    while userMove != PAPER and userMove != ROCK and userMove != SCISSORS:
        userMove = input('Input a rock, paper, or scissors: ')
        userMove = userMove.lower()
        if userMove != PAPER and userMove != ROCK and userMove != SCISSORS:
            print("You entered invalid information")
    return userMove
        

def generateMove():
    # Generate the computer's move using random.randInt().  
    # This function should return "rock", "paper", or "scissors"

    move = random.randint(1,3)
    if move == 1:
        compMove = ROCK
    elif move == 2:
        compMove = PAPER
    elif move == 3:
        compMove = SCISSORS
        
    return compMove

def calcWinner (move1, move2):

    # Compares the two moves and returns the winner. 
    # This function should return move1 or move2.  Return move1 if it is a tie

    if move1 == ROCK:
        if move2 == ROCK:
            winner = move1
        elif move2 == PAPER:
            winner = move2
        elif move2 == SCISSORS:
            winner = move1
    elif move1 == PAPER:
        if move2 == ROCK:
            winner = move1
        elif move2 == PAPER:
            winner = move1
        elif move2 == SCISSORS:
            winner = move2
    elif move1 == SCISSORS:
        if move2 == ROCK:
            winner = move2
        elif move2 == PAPER:
            winner = move1
        elif move2 == SCISSORS:
            winner = move1 
    return winner

main()
