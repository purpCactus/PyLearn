from math import sqrt

a, b, c = int(input('enter a: ')), int(input('enter b: ')), int(input('enter c: '))
delta = b ** 2 - (4 * a * c)

if delta > 0:
  x1 = -b + (sqrt(delta)) // 2 * a
  x2 = -b - (sqrt(delta)) // 2 * a
  print('the real roots are: ', x1, x2)
elif delta == 0:
  x1 = -b + (sqrt(delta)) // 2 * a
  print('the real root is: ', x1)
else: print('there are no real roots!')