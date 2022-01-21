def summation(num1, num2):
  real = num1['r'] + num2['r']
  imaginary = num1['i'] + num2['i']
  print('sum is: ', end='')
  _print(real, imaginary)


def subtraction(num1, num2):
  real = num1['r'] - num2['r']
  imaginary = num1['i'] - num2['i']
  print('subtraction is: ', end='')
  _print(real, imaginary)


def multiply(num1, num2):
  real = (num1['r'] * num2['r']) - (num1['i'] * num2['i'])
  imaginary = (num1['i'] * num2['r']) + (num1['r'] * num2['i'])
  print('multiplication is: ', end='')
  _print(real, imaginary)


def _print(real, imaginary):
  if imaginary >= 0:
    result = f'{real} +{imaginary}i'
  else: result = f'{real} {imaginary}i'
  print(result)


num1 = {'r':int(input('Enter the real part:')), 'i':int(input('enter the imaginary part:'))}
num2 = {'r':int(input('Enter the real part:')), 'i':int(input('enter the imaginary part:'))}
print('\n')
summation(num1, num2)
subtraction(num1, num2)
multiply(num1, num2)