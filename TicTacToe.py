#Tic Tac Toe
#Jason Veals
#7-2-2016
#This program allows two players to engage in a Tic Tac Toe Game
PLAY_X = "X"
PLAY_O = "O"

def main():
    board = [["*","*","*"],
             ["*","*","*"],
             ["*","*","*"]]

    ticTacToe  = False
    gameTied = False
    
    playerInstructions()
    playerX = input("Player 1 enter your name: ")
    playerO = input("Player 2 enter your name: ")

    while ticTacToe == False and gameTied == False:
        ticTacToe,gameTied = processMove(board,PLAY_X,playerX)
        if ticTacToe == False and gameTied == False:
            ticTacToe, gameTied = processMove(board,PLAY_O,playerO)

#Processes the move for each player.  
def processMove(board,move,player):
    validEntry = False
    gameTied = False
    while validEntry == False:
        row, column = playerMove(player)
        validEntry = checkEntry(board,row,column) 
    board[(row - 1)][(column - 1)] = move
    printBoard(board)
    ticTacToe = checkTicTacToe(board,move,player)
    if ticTacToe == False:
        gameTied = isGameTied(board)        
    return ticTacToe,gameTied

#Checks to see if the game is tied by searching the board array for an
#Element that contains the "*" value.  If no "*"'s are left then the game
#Is a tie
def isGameTied(board):
    gameOver = True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == "*":
                gameOver = False
    if gameOver:
        print("It's a tie")            
    return gameOver

#Checks for Tic Tac Toe in the board array by comparing the elements
#Diagonally, horizontally, and Vertically
def checkTicTacToe(board,move,player):

    #diagonal
    if board[0][0] == move and board[1][1] == move and board[2][2] == move:
        gameOver = True
    elif board[2][0] == move and board[1][1] == move and board[0][2] == move:
        gameOver = True
    #horizontal
    elif board[0][0] == move and board[0][1] == move and board[0][2] == move:
        gameOver = True
    elif board[1][0] == move and board[1][1] == move and board[1][2] == move:
        gameOver = True
    elif board[2][0] == move and board[2][1] == move and board[2][2] == move:
        gameOver = True
    #vertical
    elif board[0][0] == move and board[1][0] == move and board[2][0] == move:
        gameOver = True
    elif board[0][1] == move and board[1][1] == move and board[2][1] == move:
        gameOver = True
    elif board[0][2] == move and board[1][2] == move and board[2][2] == move:
        gameOver = True
    else:
        gameOver = False

    if gameOver:
        print("TIC-TAC-TOE")
        print(player,"wins")
    return gameOver

#Validates user input by ensuring the range for the row and columns entered
#Are valid and also checks to see if the position selected by the user
#Is available in the board array
def checkEntry(board,row,column):

    if row < 1 or row > 3:
        valid = False
        print("Invalid Entry. Number entered for row or column out of specified range")
    elif column < 1 or column > 3:
        valid = False
        print("Invalid Entry. Number entered for row or column out of specified range")
    elif board[(row - 1)][(column - 1)] == PLAY_X or board[(row - 1)][(column - 1)] == PLAY_O:
        print("That position on the board has already been taken") 
        valid = False
    else:
        valid = True
    return valid
        
#Prints user instructions for the game
def playerInstructions():
    print("Tic Tac Toe")
    print("The object of this game is to get 3 X's or 3 O's in a row")
    print("Vertically, Horizontally, or Diagonally. You will place")
    print("Your move by entering a position for the row and the column")
    print("In which you want to make your play.  For example a play in") 
    print("The center square of the board would be row 2 column 2.")
    print("Make sure your values for the rows and columns are between 1 and 3")
    print()

#Gets input from each player
def playerMove(player):
    print()
    row = int(input(player + " place your move by entering a row number "))
    column = int(input("Now enter a column number ")) 
    print()
    print()
    return row,column

#Prints the board array
def printBoard(board):
    printLine()
    for i in range(3):
        for j in range (3):
            print("|  ",board[i][j],"  |", end = "")
        print()
        printLine()
        print()

#Prints vertical line for the Tic Tac Toe board
def printLine():
    print(" ",end = "")
    for i in range(25):
        print("-",end = "")
    print()
    
main()
