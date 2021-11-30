time = input('enter time in hh:mm:ss format: ')
hour, minute, second = time.split(':')
output = int(hour) * 3600 + int(minute) * 60 + int(second)
print(output)