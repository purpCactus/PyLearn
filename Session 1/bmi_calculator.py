height = float(input('ghade khod ra be metr vared konid: '))
weight = float(input('vazne khod ra be kg vared konid: '))

bmi = weight / (height ** 2)
print('{:.2f}'.format(bmi), end=' ')

if bmi > 0 and bmi <=18.5:
  print('Underweight')
elif bmi < 25:
  print('Normal')
elif bmi < 30:
  print('Overweight')
elif bmi < 35:
  print('Obese')
else: print('Extremely Obese')
