#Keluar Permainan
def keluargame():
   print("Keluar dari permainan, Terima Kasih sudah bermain")

import random
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-",]
currentPlayer = "X"
winner = None
gameRunning = True

#Permainan bersama computer
def dengancomputer():
    #gameboard
    def printBoard(board):
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("---------")
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("---------")
        print(board[6] + " | " + board[7] + " | " + board[8])

    #Take Player input
    def playerInput(board):
        inp = int(input("Select a spot 1-9:  "))
        if board[inp-1] == "-":
           board[inp-1] = currentPlayer
        else:
           print("Oops player is already at that spot.")
           playerInput(board)

    #Check for win or tie
    def checkHorizontle(board):
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
           winner = board[2]
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
        if checkHorizontle(board):
           printBoard(board)
           print(f"the winner is {winner}!")
           gameRunning = False

        elif checkRow(board):
           printBoard(board)
           print(f"the winner is {winner}!")
           gameRunning = False

        elif checkDiag(board):
           printBoard(board)
           print(f"the winner is {winner}!")
           gameRunning = False

    def checkIfTie(board):
        global gameRunning
        if '-' not in board:
           printBoard(board)
           print("It is a tie!")
           gameRunning = False

    #Switch Player
    def switchPlayer():
        global currentPlayer
        if currentPlayer =="X":
           currentPlayer = "O"
        else:
           currentPlayer = "X"

    #System Computer
    def computer(board):
        while currentPlayer =="O":
            position = random.randint(0,8)
            if board[position] == "-":
               board[position] = "O"
               switchPlayer()

    while gameRunning:
         printBoard(board)
         playerInput(board)
         checkIfWin(board)
         if gameRunning == False:
            break
         checkIfTie(board)
         if gameRunning == False:
            break
         switchPlayer()
         computer(board)
         checkIfWin(board)
         if gameRunning ==False:
            break
         checkIfTie(board)
         if gameRunning == False:
            break

#Permainan dengan Player
def denganplayer():
    #gameboard
    def printBoard(board):
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("---------")
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("---------")
        print(board[6] + " | " + board[7] + " | " + board[8])

    #Take Player input
    def playerInput(board):
        inp = int(input("Select a spot 1-9 (X):  "))
        if board[inp-1] == "-":
           board[inp-1] = "X"
        else:
           print("Oops player is already at that spot.")
           playerInput(board)

    #Take Player 2 input
    def otherPlayer(board):
        inp = int(input("Select a spot 1-9 (O):  "))
        if board[inp-1] == "-":
           board[inp-1] = "O"
        else:
           print("Oops player is already at that spot.")
           otherPlayer(board)

    #Check for win or tie
    def checkHorizontle(board):
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
           winner = board[2]
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
        if checkHorizontle(board):
           print(f"the winner is {winner}!")
           gameRunning = False

        elif checkRow(board):
           print(f"the winner is {winner}!")
           gameRunning = False

        elif checkDiag(board):
           print(f"the winner is {winner}!")
           gameRunning = False

    def checkIfTie(board):
        global gameRunning
        if '-' not in board:
           print("It is a tie!")
           gameRunning = False

    #Switch Player
    def switchPlayer():
        global currentPlayer
        if currentPlayer =="X":
           currentPlayer = "O"
        else:
           currentPlayer = "X"

    while gameRunning:
         printBoard(board)
         playerInput(board)
         printBoard(board)
         checkIfWin(board)
         if gameRunning == False:
            break
         checkIfTie(board)
         if gameRunning == False:
            break
         switchPlayer()
         otherPlayer(board)
         checkIfWin(board)
         if gameRunning ==False:
            printBoard(board)
            break
         checkIfTie(board)
         if gameRunning == False:
            printBoard(board)
            break
         switchPlayer()

def ulang():
    board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-",]
    currentPlayer = "X"
    winner = None
    gameRunning = True
    return board, currentPlayer, winner, gameRunning

#MEMILIH JENIS GAME
print ("+-------------------------------------------------------------+")
print ("| -----", "-----", " ----", "  ", "-----", "----", " ----", "  ", "-----", " ---- ", "----- |")
print ("|   |  ", "  |  ", "|    ", "  ", "  |  ", "|  |", "|    ", "  ", "  |  ", "|    |", "|     |")
print ("|   |  ", "  |  ", "|    ", "  ", "  |  ", "----", "|    ", "  ", "  |  ", "|    |", "----- |")
print ("|   |  ", "  |  ", "|    ", "  ", "  |  ", "|  |", "|    ", "  ", "  |  ", "|    |", "|     |")
print ("|   |  ", "-----", " ----", "  ", "  |  ", "|  |", " ----", "  ", "  |  ", " ---- ", "----- |")
print ("|                       by: Angela Lisanthoni                 |")
print ("+-------------------------------------------------------------+")


main = True
while main:
    jenis = int(input("Pilih Jenis game:\n 1.Dengan Computer\n 2.Dengan Player\n 3.Keluar dari game \npilihanmu:"))
    if jenis ==1:
       print("bermain dengan computer")
       dengancomputer()
    elif jenis ==2:
       print("bermain dengan player")
       denganplayer()
    elif jenis ==3:
       main = False
       keluargame()
       break

    board, currentPlayer,winner, gameRunning = ulang()

    mainlagi = input("mau main lagi(y/n)?")
    if mainlagi == 'y':
       main = True
    elif mainlagi == 'n':
       main = False
       keluargame()
