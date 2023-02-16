# how to code this:
# create a board, display the board/update it 
# check to see if the player wins and if so reset the game
# check diagonals, rows, or columns
import random
playing = True
winner = None
current_player = "X"
gameboard = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
def showGame():
  print(gameboard[0] + " | " + gameboard[1] + " | " + gameboard[2] )
  print(gameboard[3] + " | " + gameboard[4] + " | " + gameboard[5] )
  print(gameboard[6] + " | " + gameboard[7] + " | " + gameboard[8] )
def gamePlay():
  showGame()
  
  while playing:

    playerTurn(current_player)
    checkgame()
    flipPlayer()
  if winner == "X" or winner == "O":
    print("Good job, " + str(winner) + ". You won!")
  elif winner == None:
    print("Tie.")

def playerTurn(player):
  print(player + "'s turn.")
  position = input("Choose a position from 1 to 9 (top to bottom of board): ")
  valid = False
  while not valid:
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Invalid input. Choose a position from 1 to 9: ")
    
    position = int(position) - 1
  
    if gameboard[position] == "-":
      valid = True
    else:
      print("You cannot move there! Try again.")
  

  gameboard[position] = player
  showGame()
def checkgame():
  checkwin()
  checktie()
def checkwin():
  global winner
  rowWin = checkrows()
  columnWin = checkcolumns()
  diagonalWin = checkdiagonals()
  if rowWin:
    winner = rowWin
    return
  elif columnWin:
    winner = columnWin
    return
  elif diagonalWin:
    winner = diagonalWin
    return
  else:
    winner = None
    return

def checkrows():
  global playing
  row_1 = gameboard[0] == gameboard[1] == gameboard[2] != "-"
  row_2 = gameboard[3] == gameboard[4] == gameboard[5] != "-"
  row_3 = gameboard[6] == gameboard[7] == gameboard[8] != "-"
  if row_1 or row_2 or row_3:
    playing = False
  if row_1:
    return gameboard[0]
  elif row_2:
    return gameboard[3]
  elif row_3:
    return gameboard[6]
  return


def checkcolumns():
  global playing
  column_1 = gameboard[0] == gameboard[3] == gameboard[6] != "-"
  column_2 = gameboard[1] == gameboard[4] == gameboard[7] != "-"
  column_3 = gameboard[2] == gameboard[5] == gameboard[8] != "-"
  if column_1 or column_2 or column_3:
    playing = False
  if column_1:
    return gameboard[0]
  elif column_2:
    return gameboard[1]
  elif column_3:
    return gameboard[2]
  return


def checkdiagonals():
  global playing
  dia_1 = gameboard[0] == gameboard[4] == gameboard[8] != "-"
  dia_2 = gameboard[6] == gameboard[4] == gameboard[2] != "-"
  if dia_1 or dia_2:
    playing = False
  if dia_1:
    return gameboard[0]
  elif dia_2:
    return gameboard[6]
  return


def checktie():
  global winner
  global playing
  if "-" not in gameboard and winner != "X" and winner != "O":
    playing = False
    winner = None
  return

def game2Play():
  rps = input("Rock, Paper, or Scissors? (Uppercase the first letter): ")
  rps2 = random.randint(1,3)
  if rps2 == 1:
    computer = "Rock"
  elif rps2 == 2:
    computer = "Paper"
  elif rps2 == 3:
    computer = "Scissors"
  print("The computer chose: " + computer)
  if rps == "Rock" and computer == "Paper":
    print("The computer won!")
  elif rps == "Rock" and computer == "Scissors":
    print("You beat the computer!")
  elif rps == "Paper" and computer == "Scissors":
    print("The computer won!")
  elif rps == "Paper" and computer == "Rock":
    print("You beat the computer!")
  elif rps == computer:
    print("Tie!")
  elif rps == "Scissors" and computer == "Rock":
    print("The computer won!")
  elif rps == "Scissors" and computer == "Paper":
    print("You beat the computer!")
def flipPlayer():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  return  
select = input("Tic-Tac-Toe or Rock-Paper-Scissors? (Type TTT or RPS): ")
if select == "TTT":
  gamePlay()
elif select == "RPS":
  game2Play()
else:
  print("Invalid response.")