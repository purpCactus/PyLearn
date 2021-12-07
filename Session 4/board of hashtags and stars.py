length = int(input('enter board\'s length'))
width = int(input('enter board\'s width'))

hashtag, star = '#', '*'

for i in range(width):
  for j in range(length):
    print(hashtag, end='') if j % 2 == 0 else print(star, end='')
  print()
  hashtag, star = star, hashtag
  # comment comment comment 