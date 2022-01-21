import random

WIN_MATRIX = {"ROCK": "SCISSORS",
              "SCISSORS": "PAPER",
              "PAPER": "ROCK",}

choices = ['ROCK', 'PAPER', 'SCISSORS']

user_score = 0
cpu_score = 0
turn = 0

while turn != 3:
  user = input('Enter your choice (rock, paper, scissors) > ').upper()
  cpu = random.choice(choices)
  # first simply check for the draw
  if user == cpu:
    print(cpu)
  # then check if player 1's choice trumps player 2's:
  elif WIN_MATRIX[user] == cpu:
    user_score += 1
    print(cpu)
  # then the only option left is that player 2's trumps player 1's (as the draw has been ruled out)
  else: 
    cpu_score += 1
    print(cpu)

  print(f'turn no ({turn + 1}/3)')
  turn += 1

if user_score > cpu_score:
    print('You\'re the winner.\nYour Score: ', user_score, '\nCPU Score: ', cpu_score)
elif cpu_score > user_score:
    print('CPU is the winner.\nYour Score: ', user_score, '\nCPU Score: ', cpu_score)
else: print('TIE.')
