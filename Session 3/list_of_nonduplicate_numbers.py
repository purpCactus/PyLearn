from random import randint

non_duplicate_numbers = []
length = int(input('how many numbers do you want? '))
while length > 0:
  # creating a random number
  random = randint(0, 1000)
  # checks if the random number is not already in the list
  if random not in non_duplicate_numbers:
    # then add the number to the list
    non_duplicate_numbers.append(random)
    length -= 1
  # if it was already in the list, then continue
  else: continue

print(non_duplicate_numbers)