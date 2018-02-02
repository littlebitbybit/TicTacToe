plays = [[" " for r in range(3)] for c in range(3)] 

def print_board():
	print(plays[0][0] + ' | ' + plays[0][1] + ' | ' + plays[0][2])
	print('__' + '|' + '___' + '|' + '__')
	print(plays[1][0] + ' | ' + plays[1][1] + ' | ' + plays[1][2])
	print('__' + '|' + '___' + '|' + '__')
	print(plays[2][0] + ' | ' + plays[2][1] + ' | ' + plays[2][2])
	print('  ' + '|' + '   ' + '|' + '  ')

def make_move(row, col, player):
	assert plays[row][col] == " ", 'Slot is already filled!'
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
	if plays[0][2] == plays[1][1] and plays[1][1] == plays[2][0]  and plays[0][2] != " ":
		return True
	return False

def check_tie():
	for rows in plays:
		for col in rows:
			if col == ' ':
				return False
	return True

def start():
	turn_x = True
	current_player = 'x'
	while True:
		

		if turn_x:
			print("Player 1 (x): ")
		else:
			print("Player 2 (o): ")

		move_row = None
		move_col = None
		while move_row is None or move_col is None:
			try:
				move_row = int(input("Row: "))
				assert 0 <= move_row <= 2, 'Invalid row (Must be between 0-2)'
				move_col = int(input("Col: "))
				assert 0 <= move_col <= 2, 'Invalid column (Must be between 0-2)'

				make_move(move_row, move_col, current_player)
			except (TypeError, AssertionError) as e:
				print(e)
				move_col = move_row = None

		print_board()
		if check_win():
			print(current_player + " won!")
			break
		elif check_tie():
			print("tie!")
			break
		else:
			turn_x = not turn_x
			if turn_x:
				current_player = 'x'
			else:
				current_player = 'o'

start()

