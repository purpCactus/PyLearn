seconds = int(input('enter time in seconds: '))
hour = seconds // 3600
seconds -= hour * 3600
minute = seconds // 60
seconds -= minute * 60
print(f'{hour}:{minute}:{seconds}')