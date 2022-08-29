import random

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput(board):
    inp = int(input("SELECT POSITION: "))
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("ALREADY OCCUPIED")

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True

def checkIfWin(board):
    global gameRunning
    if checkHorizontal(board):
        printBoard(board)
        print(f"{winner} WINS!")
        gameRunning = False

    elif checkRow(board):
        printBoard(board)
        print(f"{winner} WINS!")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print(f"{winner} WINS!")
        gameRunning = False

def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("MATCH DRAW!")
        gameRunning = False

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

if __name__ == "__main__":
    while gameRunning:
        print("*** SELECT 1 TO 9 TO OCCCUPY POSITION IN BOARD ***")
        print("PLAYER = X")
        print("COMPUTER = O")
        printBoard(board)
        playerInput(board)
        checkIfWin(board)
        checkIfTie(board)
        switchPlayer()
        computer(board)
        checkIfWin(board)
        checkIfTie(board)