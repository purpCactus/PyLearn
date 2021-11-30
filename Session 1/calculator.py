import math

operator = int(input('what do you want to do?\n1.sum\n2.minus\n3.multiply\n4.divide\n5.radical\n6.sin\n7.cos\n8.tan\n9.factorial\n> '))
if operator > 0 and operator < 5:
  num1 = int(input('adade aval ra vared konid: '))
  num2 = int(input('adade dovom ra vared konid: '))
elif operator > 4 and operator < 10:
  num1 = int(input('adade morede nazar ra vared konid: '))
# 4amale asli
if operator == 1:
  answer = num1 + num2
elif operator == 2:
  answer = num1 - num2
elif operator == 3:
  answer = num1 * num2
elif operator == 4:
  if num2 is not 0:
    answer = num1 / num2
  else: print('Cannot divide by zero')
elif operator == 5:
  answer = math.sqrt(num1)
elif operator == 6:
  answer = math.sin(math.radians(num1))
elif operator == 7:
  answer = math.cos(math.radians(num1))
elif operator == 8:
  answer = math.tan(math.radians(num1))
elif operator == 9:
  answer = math.factorial(num1)
else: print('invalid operator number!')
print(answer)