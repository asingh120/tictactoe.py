''' Command line based game of Tic Tac Toe. User is asked for 
	position number on grid from 1-9. Next player is then asked for 
	position number. Player switch goes on till there is a winner or a tie '''

#--- Global Variables

#Game board
board = ["-","-","-",
		 "-","-","-",
		 "-","-","-"]


#If game is still going
game_still_going = True

#Who won? Or tie?
winner = None

#Whose turn is it?
current_player = "X"


def displayBoard():
	#Creates tic tac toe board
	print(board[0] + "|" + board[1] + "|" + board[2])
	print(board[3] + "|" + board[4] + "|" + board[5])
	print(board[6] + "|" + board[7] + "|" + board[8])

#Play game of tic tac toe
def playGame():
	#Display initial board
	displayBoard()

	#Loop while game is still going
	while game_still_going:
		#Handle single turn of player
		handleTurn(current_player)

		#Check if game has ended
		check_if_game_over()

		#Flip between players
		flipPlayer()

	#The Game has ended
	if winner == "X" or winner == "O":
		print(winner + " won!")
	elif winner == None:
		print("Game is tied!")


def handleTurn(player):

	print(player + "'s turn.")
	#Asks user to enter position number
	position = input("Choose a position from 1-9: >> ")

	#Loop to determine if position selected is filled or empty, and that user input is only within parameters
	valid = False
	while not valid:
		while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
			position = input("Choose a position 1-9: ")

		position = int(position) - 1

		#If position is already filled, user is prompted to enter another position
		if board[position] == "-":
			valid = True
		else:
			print("You can't go there. Go again!")



	#Assign user input into board position
	board[position] = player
	displayBoard()


def check_if_game_over():
	checkWinner()
	checkTie()


def checkWinner():

	#Set up global variables
	global winner

	#Checks rows
	row_winner = checkRows()

	#Checks columns
	column_winner = checkColumns()

	#Checks diagonals
	diagonal_winner = checkDiagonals()

	if row_winner:
		#There was a win
		winner = row_winner
	elif column_winner:
		#There was a win
		winner = column_winner
	elif diagonal_winner:
		#There was a win
		winner = diagonal_winner
	else:
		#There was no win
		winner = None

	return


def checkRows():
	#Set up global variables
	global game_still_going

	#Check if any of the rows have the same value and is not empty
	row_1 = board[0] == board[1] == board[2] !="-"
	row_2 = board[3] == board[4] == board[5] !="-"
	row_3 = board[6] == board[7] == board[8] !="-"

	#If any row has a match, stop the game 
	if row_1 or row_2 or row_3:
		game_still_going = False

	#Return winner (X or O)
	if row_1:
		return	board[0]
	elif row_2:
		return board[3]
	elif row_3:
		return board[6]
	return


def checkColumns():
	#Set up global variables
	global game_still_going

	#Check if any of the rows have the same value and is not empty
	column_1 = board[0] == board[3] == board[6] !="-"
	column_2 = board[1] == board[4] == board[7] !="-"
	column_3 = board[2] == board[5] == board[8] !="-"

	#If any row has a match, stop the game 
	if column_1 or column_2 or column_3:
		game_still_going = False

	#Return winner (X or O)
	if column_1:
		return	board[0]
	elif column_2:
		return board[1]
	elif column_3:
		return board[2]
	return

def checkDiagonals():
	#Set up global variables
	global game_still_going

	#Check if any of the rows have the same value and is not empty
	diagonal_1 = board[0] == board[4] == board[8] !="-"
	diagonal_2 = board[2] == board[4] == board[6] !="-"

	#If any row has a match, stop the game 
	if diagonal_1 or diagonal_2:
		game_still_going = False

	#Return winner (X or O)
	if diagonal_1:
		return	board[0]
	elif diagonal_2:
		return board[6]
	return

def checkTie():
	#Global variables we need
	global game_still_going

	if "-" not in board:
		game_still_going = False
	return


def flipPlayer():
	#Global variables we need
	global current_player
	#if current play was X, change to O
	if current_player == "X":
		current_player = "O"
	#if current player was O, change to X
	elif current_player == "O":
		current_player = "X"
	return

playGame()

