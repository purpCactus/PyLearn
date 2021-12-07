length, width = int(input('enter length: ')), int(input('enter width: '))

for i in range(1, width + 1):
  for j in range(1, length + 1):
    print(f'{i * j}'.expandtabs(1), end='\t')
  print()