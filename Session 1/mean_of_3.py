first_name, last_name = input('Enter your first name: '), input('Enter your last name: ')
grades = []
for i in range(3):
  grades.append(int(input(f'nomre darse {i + 1} ra vared konid: ')))
mean = sum(grades) / len(grades)
if mean > 0 and mean < 12:
  print('Fail')
elif mean < 17:
  print('Normal')
elif mean >= 17:
  print('Great')