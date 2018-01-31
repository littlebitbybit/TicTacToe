plays = [[" " for r in range(3)] for c in range(3)] 

def print_board():
	print(plays[0][0] + ' | ' + plays[0][1] + '| ' + plays[0][2])
	print('__' + '|' + '__' + '|' + '__')
	print(plays[1][0] + ' | ' + plays[1][1] + '| ' + plays[1][2])
	print('__' + '|' + '__' + '|' + '__')
	print(plays[2][0] + ' | ' + plays[2][1] + '| ' + plays[2][2])
	print('  ' + '|' + '  ' + '|' + '  ')

def make_move(row, col, player):
	#currently allows you to make move if someone already made a move there
	plays[row][col] = player


def check_win():
	for i in range(3):
		if plays[0][i] == plays[1][i] and plays[1][i] == plays[2][i] and plays[0][i] != " ":
			#check columns
			return True
		elif plays[i][0] == plays[i][1] and plays[i][1] == plays[i][2] and plays[i][0] != " ":
			#check rows
			return True
	if plays[0][0] == plays[1][1] and plays[1][1] == plays[2][2]  and plays[0][0] != " ":
		return True
	return False


def start():
	turn_x = True
	current_player = 'x'
	while True:
		

		if turn_x:
			print("Player 1 (x): ")
		else:
			print("Player 2 (o): ")

		try:
			move_row = int(input("Row: "))
			move_col = int(input("Col: "))
			#currently allows you to input ints past 2
		except:
			print ("input valid number between 0-2")


		make_move(move_row, move_col, current_player)
		print_board()
		if check_win():
			print(current_player + " won!")
			break
		else:
			turn_x = not turn_x
			if turn_x:
				current_player = 'x'
			else:
				current_player = 'y'

start()

