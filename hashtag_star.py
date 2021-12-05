length = int(input('Enter the desired length: '))

for i in range(length):
  if i % 2 == 0:
    print('*', end='')
  else: print('#', end='')
