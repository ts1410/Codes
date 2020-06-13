# Uses python3
import sys

def lcm_naive(a, b):
    if min(a, b) == 0:
        return 0
    p = a*b
    while b != 0:
        a, b = b, a%b
    return p//a

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

