# we can input data in different ways, for example:
# one-line input:

# first way:
length = int(input('enter the length of list: '))

# first it'll split the input then convert it to int with map(), and then it'll return a list and it goes till length is reached.
numbers_list = list(map(int, input('enter the numbers: ').split()))[:length]

# second way:
# it'll split the input data, then convert it to int with for loop.
numbers_list = [int(item) for item in input('enter the numbers: ').split()]

# sorting the list in ascending order
sort = sorted(numbers_list)

# checks if the list is in ascending order
if sort == numbers_list:
  print('The list is in Ascending order!')
else: print('The list is not in Ascending order!')

#-------------------------------------------------
# multiple line inputs:

# third way:
try:
  numbers_list = []
  while True:
    numbers_list.append(int(input('enter a number: ')))
# and in case of any error, it'll run this part
except:
  sort = sorted(numbers_list)  
  if sort == numbers_list:
    print('The list is in Ascending order!')
  else: print('The list is not in Ascending order!')


