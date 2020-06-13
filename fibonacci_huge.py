# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    F = [0, 1]
    a = 1
    b = 1
    count = 1
    while True:
        a, b = b, (a+b)%m
        count += 1
        if a == 0 and b == 1:
            break
        F.append(a)
    n = n%count
    return F[n]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
