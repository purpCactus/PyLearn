from random import randint
import random

while True:
  random_number = randint(1, 6)
  print(random_number)
  if random_number == 6:
    continue
  elif input('you wanna go again? y/n: ') == 'y':
    continue
  else: break
