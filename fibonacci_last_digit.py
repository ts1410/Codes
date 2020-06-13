# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n<=1:
        return n
    f = [0]*(n+1)
    f[1] = 1
    for i in range(2, n+1):
        f[i] = (f[i-1] + f[i-2])%10

    return f[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
