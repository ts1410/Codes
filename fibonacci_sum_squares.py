# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    n = n % 60
    if n <= 1:
        return n
    a = 0
    b = 1
    s = 1
    for i in range(2, n + 1):
        s = (s + ((a + b)**2)%10)%10
        a, b = b, (a + b)%10

    return s

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
