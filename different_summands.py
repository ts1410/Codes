# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    i = 1
    s = 0
    while s + i <= n:
        s += i
        summands.append(i)
        i += 1
    summands[len(summands) - 1] += n - s
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
