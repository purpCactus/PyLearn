from random import choice

# our collection of words
words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmohs']

# choosing a word from collection
answer = choice(words)
answer_length = len(answer)

# number of chances user has
hp = answer_length

# creating the hangman
text = list('-' * answer_length)
print(''.join(text))
wrong = ''

while hp > 0:
  # checks if user has won
  if ''.join(text) == answer:
    won = True
    break
  # checks if the user letter was found in the answer
  found = False
  won = False
  user_input = input('enter a letter: ').lower()
  # iterate through answer and checks if user entered the right letter
  for num, letter in enumerate(list(answer)):
    # if found, replace '-' with the letter
    if letter == user_input:
      text[num] = user_input
      found = True
  # if not, decrements chances
  if not found:
    wrong += user_input
    hp -= 1
  print(''.join(text))
  print(wrong)
  print(f'You\'ve {hp} chances left!')

if won:
  print('\n\nCongrats! You\'ve won!\n\n')
else: print('Sorry! better luck next time.')