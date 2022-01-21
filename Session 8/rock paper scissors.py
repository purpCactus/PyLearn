import random


user_score = 0
cpu_score = 0 
while True:
  choices = ['rock', 'paper', 'scissors']
  cpu_choice = random.choice(choices)

  user_input = input('Enter your choice (rock, paper, scissors) -> ').lower()

  if user_input == 'rock':
    if cpu_choice == 'rock':
      print('Cpu choice: ', cpu_choice, '\nTie.')
    elif cpu_choice == 'paper':
      print('Cpu choice: ', cpu_choice, '\nYou\'ve lost.')
      cpu_score += 1
    elif cpu_choice == 'scissors':
      print('Cpu choice: ', cpu_choice, '\nYou\'ve won.')
      user_score += 1
  elif user_input == 'paper':
    if cpu_choice == 'rock':
      print('Cpu choice: ', cpu_choice, '\nYou\'ve won.')
      user_score += 1
    elif cpu_choice == 'paper':
      print('Cpu choice: ', cpu_choice, '\nTie.')
    elif cpu_choice == 'scissors':
      print('Cpu choice: ', cpu_choice, '\nYou\'ve lost.')
      cpu_score += 1
  elif user_input == 'scissors':
    if cpu_choice == 'rock':
      print('Cpu choice: ', cpu_choice, '\nYou\'ve won.')
      user_score += 1
    elif cpu_choice == 'paper':
      print('Cpu choice: ', cpu_choice, '\nYou\'ve lost.')
      cpu_score += 1
    elif cpu_choice == 'scissors':
      print('Cpu choice: ', cpu_choice, 'Tie.')
  else: 
    print('Try again, this time with valid input.')
    continue
  print('Your score is: ', user_score, '\nCpu score is: ', cpu_score)
  if user_score == 3:
    print('\nYou\'ve won the match.')
    break
  elif cpu_score == 3:
    print('\nYou\'ve lost the match.')
    break
