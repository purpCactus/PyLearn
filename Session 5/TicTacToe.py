import timeit
from random import randint


# global variables
# the board
game_board = [['-', '-', '-'],
              ['-', '-', '-'],
              ['-', '-', '-']]
# turn number for using it to see who's turn is it
turn_no = 1

# for printing the board
def show_board():
  for row in game_board:
    for item in row:
      if item == '-':
        print('\33[33m' + item + '\33[0m', end=' ')
      elif item == 'X':
        print('\33[31m' + item + '\33[0m', end=' ')
      else: print('\33[32m' + item + '\33[0m', end=' ')
    print()


# to see who's turn is it
def turn(turn_no):
  return 'X' if turn_no % 2 == 1 else 'O'


# checks if the board is full
def game_over():
  # how many rows are full?
  cnt = 0
  for row in game_board:
    if '-' not in row:
      cnt += 1
  # if all of the rows are full then return True
  if cnt == 3:
    return True
  else: return False


# checks the winning conditions
def win_check():
  # Horizontal
  for idx, row in enumerate(game_board):
    if row[idx] != '-' and all(item == row[idx] for item in row):
      return True
  # Vertical
  for i in range(3):
    if game_board[0][i] != '-' and all(game_board[j][i] == game_board[0][i] for j in range(3)):
      return True
  # Diagonal
  if game_board[1][1] != '-' and all(game_board[j][j] == game_board[1][1] for j in range(0, 3, 2)):
    return True
  if game_board[1][1] != '-' and game_board[1][1] == game_board[0][2] and game_board[1][1] == game_board[2][0]:
    return True


# checks for the tie condition
def tie_check():
  if not win_check() and game_over():
    return True


# game's body
def game(turn_no, game_type):
  # goes until the board is full
  while not game_over():
    # check for the game type. single player or multiplayer
    if game_type == 2:
      # if it's user's turn: show the board and take user's spot
      if turn_no % 2 == 1:
        show_board()
        spot = int(input(f'{turn(turn_no)}\'s turn.\nEnter a spot between 1-9: ')) - 1
      # if it's computer's turn: create a random number between 0 and 8
      else: spot = randint(0, 8)
    # if playing with a friend:
    else:
       show_board()
       spot = int(input(f'{turn(turn_no)}\'s turn.\nEnter a spot between 1-9: ')) - 1
    # it's a 2d array, here we create the i and j indices
    row, col = spot // 3, spot % 3
    # if the spot is empty: fill it, and check for winningg conditions
    if game_board[row][col] == '-':
      game_board[row][col] = turn(turn_no)
      if win_check():
        show_board()
        print('\n\n\33[35m', turn(turn_no), 'IS THE WINNER.\n\33[0m')
        break
      turn_no += 1
    # if not tell the user choose another spot
    elif turn_no % 2 == 1 or game_type == 1: 
      print('spot is already filled, enter another number.')
  # after the board is full it checks for the tie condition
  if tie_check():
    show_board()
    print('It\'s a Tie!')


# menu
def menu():
  return int(input('Welcome.\n\t1.With a Friend\t\t2.With Computer\n\t> ')) 


# DRIVER CODE
# track the application run time
start = timeit.default_timer()
# get's the user input from menu
game_type = menu()
# play's the game
game(turn_no, game_type)
# stops the application run time
stop = timeit.default_timer()
print('\33[34m Time: {:.2f}'.format(stop - start), 'seconds.\33[0m')
