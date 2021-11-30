numbers = []
while True:
  user_input = input('enter a number else enter exit: ')
  if user_input.isnumeric():
    numbers.append(int(user_input))
  else:
    break

print(sum(numbers))