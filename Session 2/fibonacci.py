n = int(input('how many fibonacci numbers do you want? '))

def Fibonacci(n):
    if n < 0:
        print('incorrect input')
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

fibonacci_sequence = []
for i in range(1, n + 1):
  fibonacci_sequence.append(Fibonacci(i))
print(fibonacci_sequence)