def summation(frc1, frc2): 
  num1 = frc1['numerator'] * frc2['denominator']
  denominator = frc1['denominator'] * frc2['denominator']
  num2 = frc2['numerator'] * frc1['denominator']
  result = num1 + num2
  _print(result, denominator)


def subtraction(frc1, frc2):
  num1 = frc1['numerator'] * frc2['denominator']
  denominator = frc1['denominator'] * frc2['denominator']
  num2 = frc2['numerator'] * frc1['denominator']
  result = num1 - num2
  _print(result, denominator)


def multiplication(frc1, frc2):
  numerator = frc1['numerator'] * frc2['numerator']
  denominator = frc1['denominator'] * frc2['denominator']
  _print(numerator, denominator)


def _print(result, denominator):
  result = f'{result}/{denominator}'
  print(result)


def division(frc1, frc2):
  reciprocal = {'numerator': frc2['denominator'], 'denominator': frc2['numerator']}
  multiplication(frc1, reciprocal)


frc1 = {'numerator': int(input('Enter the numerator: ')), 'denominator': int(input('Enter the denominator: '))}
frc2 = {'numerator': int(input('Enter the numerator: ')), 'denominator': int(input('Enter the denominator: '))}
summation(frc1, frc2)
subtraction(frc1, frc2)
multiplication(frc1, frc2)